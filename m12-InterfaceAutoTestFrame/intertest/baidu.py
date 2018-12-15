# # ==========================
# # 1、常规的百度搜索接口测试
# # ==========================
# import requests
# url = "https://www.baidu.com/s"
# params = {
#     "wd": "leo"
# }
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
#
# r = requests.get(url, params, headers=headers)
#
# print(r.text)



# # ===========================================
# # 2、使用封装的requests模块框架进行优化
# # ===========================================#
# from common.confighttp import ConfigHttp
# url = "/s"
# params = {
#     "wd": "leo"
# }
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
#
# bd_search_request = ConfigHttp("HTTP", "host", "port", "timeout")
# bd_search_request.set_url(url)
# bd_search_request.set_params(params)
# bd_search_request.set_headers(headers)
# r = bd_search_request.get()
# print(r.text)

# # ==================================================
# # 3、数据分离，从EXCEL中读取测试接口和测试用例
# # =================================================
# from common.doexcel import DoExcel
# from common.confighttp import ConfigHttp
#
#
# excel = DoExcel("case.xls", "Sheet1")
# row_num = excel.get_row_num(0, "bd-001")
# url = excel.read_cell(row_num, 2).value
# params = {
#     "wd": "leo"
# }
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
#
#
# new_request = ConfigHttp("HTTP", "host", "port", "timeout")
# new_request.set_url(url)
# new_request.set_params(params)
# new_request.set_headers(headers)
# r = new_request.get()
# print(r.text)

# # ==========================================================================================
# # 4、在3的基础上优化：判断excel中实际结果的单元格是否为空，为空则写入，不为空则先输出再覆盖
# # ==========================================================================================
# from common.doexcel import DoExcel
# from common.confighttp import ConfigHttp
#
#
# excel = DoExcel("case.xls", "Sheet1")
# row_num = excel.get_row_num(0, "bd-001")
# url = excel.read_cell(row_num, 2).value
# params = {
#     "wd": "leo"
# }
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
#
#
# new_request = ConfigHttp("HTTP", "host", "port", "timeout")
# new_request.set_url(url)
# new_request.set_params(params)
# new_request.set_headers(headers)
# r = new_request.get()
# print(r.status_code)
#
# cell_value = excel.read_cell(row_num, 10).value
# if cell_value:
#     print("第 {}", 10, "个单元格不为空，现有数据为：", cell_value)
#     excel.write_excel(0, row_num, 10, r.status_code)
# else:
#     print("第 {}", 10, "个单元格不为空")
# excel.write_excel(0, row_num, 10, r.status_code)

# ==========================================================================================
# 5、在4的基础上优化
# 目的：封装成类
# ==========================================================================================
from common.doexcel import DoExcel
from common.confighttp import ConfigHttp

params = {
    "wd": "leo"
}
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

class Baidu:
    def __init__(self, excel_name, sheet_name):
        '''
        初始化DoExcel和ConfigHttp
        '''
        self.excel = DoExcel(excel_name, sheet_name)
        self.row_num = self.excel.get_row_num(0, "bd-001")
        self.excel.write_excel(0, self.row_num, 10, None)
        self.new_request = ConfigHttp("HTTP", "host", "port", "timeout")
        self.url  = self.excel.read_cell(self.row_num, 2)

    def baidu_get(self):
        self.new_request.set_url(url=self.url)
        self.new_request.set_headers(headers)
        self.new_request.set_params(params=params)
        r = self.new_request.get()
        print(r.status_code)
        self.excel.write_excel(0, self.row_num, 10, r.status_code)
        return r.status_code

# ===================================
# 测试代码
# ===================================
baidu = Baidu("case.xls", "baidu")
baidu.baidu_get()