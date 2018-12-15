import os
import configparser

# 当前文件所在目录
file_dir = os.path.split(os.path.realpath(__file__))[0]
# 配置文件的完整路径
confini_path = os.path.join(file_dir, "config.ini")

class ReadConfig:
    '''读取配置文件'''

    def __init__(self):
        self.cf = configparser.ConfigParser()
        # 直接配置好默认的配置文件路径，避免别处用到该类时每次都要获取
        self.cf.read(confini_path, encoding="utf-8")

    def get_config_value(self, section, name):
        '''获取配置文件中的配置项值'''
        return self.cf.get(section, name)

    def get_email_config(self, name):
        '''获取email配置的相关值'''
        return self.cf.get("EMAIL", name)




# =============================================================
# 验证ReadConfig的正确性
# 当前类所在目录
# file_path = os.path.split(os.path.realpath(__file__))[0]
# read_conf = ReadConfig(os.path.join(file_path, "config.ini"))
# value = read_conf.get_config_value("HTTP", "host")
# print(value)
# ==============================================================