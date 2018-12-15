import logging
import os
import time


log_dir = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "log")
class Logger:

    def __init__(self, logger, cmd_log_level, file_log_level):
        '''
        日志模块，将日志的操作进行封装，对日志级别再次进行封装
        :param logger: 
        :param cmd_log_level: 控制台日志级别
        :param file_log_level: 文件日志级别
        '''
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

        #设置文件日志名称
        self.log_file_name = os.path.join(log_dir, "{0}.log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(cmd_log_level)

        #设置文件日志
        fh = logging.FileHandler(self.log_file_name)
        fh.setFormatter(fmt)
        fh.setLevel(file_log_level)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        '''重写日志的debug方法'''
        self.logger.debug(message)

    def info(self, message):
        '''重写日志的info方法'''
        self.logger.info(message)

    def warning(self, message):
        '''重写日志的warning方法'''
        self.logger.warning(message)

    def error(self, message):
        '''重写日志的error方法'''
        self.logger.error(message)

    def critical(self, message):
        '''重写日志的critical方法'''
        self.logger.critical(message)


if __name__ == "__main__":
    logger = Logger("FOX", cmd_log_level=logging.INFO, file_log_level=logging.ERROR)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")