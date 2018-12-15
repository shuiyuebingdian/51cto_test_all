
# =====================================================================
# 将get_weixin_access_token.py和wx_send_message_all.py整合优化为一个类
# =====================================================================
from common.confighttp import ConfigHttp
from common.doexcel import DoExcel

get_token_url = "/cgi-bin/token"
get_token_params = {
    "grant_type": "client_credential",
    "appID": "wxd4af3f5a7728eb1b",
    "secret": "12d7130a01722a8d937c7046d3aa2e96"
}

send_message_data = {
    "filter": {
        "is_to_all": True
    },
    "text":{
        "content": "weixin send message to all"
    },
    "msgtype": "text"
}

class WeiXin:

    def __init__(self, test_case_excel):
        self.test_data_excel = test_case_excel
        self.new_request = ConfigHttp("HTTP2", "host", "port", "timeout")

    def get_token(self):
        row_num = self.test_data_excel.get_row_num(0, "weixin-001")
        self.new_request.set_url(get_token_url)
        self.new_request.set_params(get_token_params)
        res = self.new_request.get()
        self.test_data_excel.write_excel(0, row_num, 6, res.text)
        return res

    def send_message(self):

        access_token = self.get_token()

        if access_token:
            row_num = self.test_data_excel.get_row_num(0, "weixin-002")
            url = self.test_data_excel.read_cell(row_num, 2)
            self.new_request.set_url(url)
            self.new_request.set_data(data=send_message_data)
            params = {
                "access_token": access_token
            }
            self.new_request.set_params(params)
            r = self.new_request.post()
            errmsg = r.json()["errmsg"]
            if errmsg == "send job submission success" or errmsg == "clientmsgid exist":
                self.test_data_excel.write_excel(0, row_num, 10, errmsg)
            else:
                print("send job submission fail")
        else:
            print("access_token is null")

# ======================
# 测试代码
# ======================
excel = DoExcel("case.xls", "weixin")
wei_xin = WeiXin(excel)
wei_xin.get_token()
