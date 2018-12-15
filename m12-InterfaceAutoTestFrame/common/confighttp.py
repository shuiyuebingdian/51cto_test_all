import requests
from config.readconfig import ReadConfig
from log.logger import Logger
read_config = ReadConfig()

class ConfigHttp():

    def __init__(self, section, host, port, timeout):
        '''
        读取配置config.ini文件中的全局配置信息
        :param section 配置文件中【节】的名字
        :param host: 配置文件中name的名字
        :param port: 配置文件中name的名字
        :param timeout: 配置文件中name的名字
        '''
        self.host = read_config.get_config_value(section, host)
        self.port = read_config.get_config_value(section, port)
        self.timeout = read_config.get_config_value(section, timeout)
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        # self.log = Logger.get_log()
        # self.logger = self.log.get_logger()


    def set_url(self, url):
        '''拼接完整的接口测试地址'''
        self.url = self.host + url

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_data(self, data):
        self.data = data

    def set_files(self, files):
        self.files = files

    def get(self):
        '''重写GET方法'''
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post(self):
        '''重写POST方法'''
        try:
            response = requests.post(self.url, data=self.data, headers=self.headers, files=self.files, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

# =============================================================
# 验证ConfigHttp的正确性

config_http = ConfigHttp("HTTP", "host", "port", "timeout")
config_http.set_url("/s")
response = config_http.get()
print(response)
# read_conf = ReadConfig(os.path.join(file_path, "config.ini"))
# value = read_conf.get_config_value("HTTP", "host")
# print(value)
# ==============================================================