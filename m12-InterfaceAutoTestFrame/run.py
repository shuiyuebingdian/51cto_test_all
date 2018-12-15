from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import common.sendmail as cc
import os

test_report_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0], "testreport")
def AutoRun(test_case_name):
    '''
    
    :param TestCaseName: 测试用例文件名
    :return: 
    '''
    discover = unittest.defaultTestLoader.discover(test_report_dir, pattern=test_case_name)

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = test_report_dir + "\\" + now + "result.html"
    fp = open(file_name, "wb")
    runner = HTMLTestRunner(stream=fp, title="接口测试报告", description="接口测试用例执行情况")
    runner.run(discover)
    fp.close()

    new_report = cc.get_new_report(test_report_dir)
    cc.send_report(new_report)

if __name__ == "__main__":
    AutoRun("weixin_tc.py")

