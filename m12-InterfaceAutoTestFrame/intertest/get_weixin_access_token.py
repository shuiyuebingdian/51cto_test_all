# # ===========================
# # 1、常规方式获得Access_token
# # ===========================
# import requests
#
# # 获取access_token的接口地址
# url = "https://api.weixin.qq.com/cgi-bin/token"
# params = {
#     "grant_type": "client_credential",
#     "appID": "wxd4af3f5a7728eb1b",
#     "secret": "12d7130a01722a8d937c7046d3aa2e96"
# }
#
# r = requests.get(url, params)
# print(r.text)

# ===========================================
# 2、对方式1进行优化封装
# ===========================================
from common.confighttp import ConfigHttp
from common.doexcel import DoExcel

url = "/cgi-bin/token"
params = {
    "grant_type": "client_credential",
    "appID": "wxd4af3f5a7728eb1b",
    "secret": "12d7130a01722a8d937c7046d3aa2e96"
}

class GetToken:
    def __init__(self):
        self.test_data_excel = DoExcel("case.xls", "weixin")
        self.row_num = self.test_data_excel.get_row_num(0, "weixin-001")
        self.new_request = ConfigHttp("HTTP2", "host", "port", "timeout")

    def get_token(self):
        self.new_request.set_url(url)
        self.new_request.set_params(params)
        res = self.new_request.get()
        self.test_data_excel.write_excel(0, self.row_num, 6, res.text)
        return res

wei_xin_token = GetToken()
wei_xin_token.get_token()
