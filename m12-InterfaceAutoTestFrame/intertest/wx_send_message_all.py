from common.confighttp import ConfigHttp
from common.doexcel import DoExcel

data = {
    "filter": {
        "is_to_all": True
    },
    "text":{
        "content": "weixin send message to all"
    },
    "msgtype": "text"
}
class WeiXinSendMessage:
    def __init__(self, excel_name, sheet_name):
        self.excel = DoExcel(excel_name, sheet_name)
        self.row_num = self.excel.get_row_num(0, "weixin-002")
        self.url = self.excel.read_cell(self.row_num, 2)
        self.new_request = ConfigHttp("HTTP2", "host", "port", "timeout")

    def send_message(self):
        row_num = self.excel.get_row_num(0, "weixin-001")
        access_token = self.excel.read_cell(row_num, 6)
        params = {
            "access_token": access_token
        }
        if access_token:
            self.new_request.set_url(self.url)
            self.new_request.set_data(data=data)
            self.new_request.set_params(params)
            r = self.new_request.post()
            errmsg = r.json()["errmsg"]
            if errmsg == "send job submission success" or errmsg == "clientmsgid exist":
                self.excel.write_excel(0, self.row_num, 10, errmsg)
            else:
                print("send job submission fail")
        else:
            print("access_token is null")

# =========================================
# 测试代码
# =========================================
weixin = WeiXinSendMessage("case.xls", "weixin")
weixin.send_message()
