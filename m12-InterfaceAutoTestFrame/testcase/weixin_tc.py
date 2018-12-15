
import unittest
import logging
from intertest.weixin import WeiXin
from log.logger import Logger
from common.doexcel import DoExcel

class WeiXinTest(unittest.TestCase):
    '''微信公众号测试'''

    def setUp(self):
        self.excel = DoExcel("case.xls", "weixin")
        self.weixin = WeiXin(self.excel)
        self.logger = Logger("FOX", cmd_log_level=logging.INFO, file_log_level=logging.INFO)

    def test_get_token(self):
        access_token = self.weixin.get_token().json()["access_token"]
        print(access_token)
        row_num = self.excel.get_row_num(0, "weixin-001")
        self.excel.write_excel(0, row_num, 6, access_token)

    def test_post_message(self):
        self.weixin.send_message()
        row_num = self.excel.get_row_num(0, "weixin-002")
        result = self.excel.read_cell(row_num, 10)
        self.assertEqual(result, "pass")


    def tearDown(self):
        pass

# =============================
# 测试代码
# =============================
if __name__ == "__main__":
    unittest.main()

