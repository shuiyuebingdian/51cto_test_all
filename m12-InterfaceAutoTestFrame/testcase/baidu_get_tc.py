
import unittest
import logging
from intertest.baidu import Baidu
from log.logger import Logger

class BaiDuGet(unittest.TestCase):
    '''百度get测试，带headers'''

    def setUp(self):
        self.baidu = Baidu("case.xls", "baidu")
        self.logger = Logger("FOX", cmd_log_level=logging.INFO, file_log_level=logging.INFO)

    def test_baidu_get(self):
        try:
            status_code = self.baidu.baidu_get()
            self.assertEqual(status_code, 200)
            self.logger.info("baidu get success")
        except BaseException as e:
            self.logger.error("baidu get fail")
            raise

    def tearDown(self):
        pass

# =============================
# 测试代码
# =============================
if __name__ == "__main__":
    unittest.main()

