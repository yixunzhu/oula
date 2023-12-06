# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2021/6/4'

import os
import time
import logging

# 创建存放log的目录
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Logs(object):
    def __init__(self):
        # 创建日志文件
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        # 第一步，创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  # Log等级开关
        # 设置log的输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s]-%(levelname)s:%(message)s')
        self.formatter = ""

    def __console(self, level, message):
        file = logging.FileHandler(self.logname, 'a+', encoding='utf-8')
        # debug类型只输入到log文件
        file.setLevel(logging.DEBUG)
        # 设置输入的格式
        file.setFormatter(self.formatter)
        # 加入到log文件
        self.logger.addHandler(file)
        # 输入控制台和log文件
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        # 加入到log文件
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            # 捕获代码异常（traceback）
            self.logger.exception(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(file)
        file.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    print(log_path)
    log = Logs()
    # log.debug('test123')
    # log.warning("test")
    # log.info("123")
    sql = """
        INSERT INTO public.yanshou_ceshi
            (
                HANDLE_MONTH,
                LATN_ID,
                SERV_CODE,
                ACCT_ITEM_TYPE_CODE,
                ACCT_PERIOD,
                ACCT_MONTH,
                OWE_AMOUNT,
                UNCONFIRM_OWE,
                CONFIRM_OWE,
                PAY_TYPE
            )
            VALUES
            (
                '202111',
                'LATN{}',
                'SERV003',
                'ITEM003',
                'PERIOD003',
                'MONTH003',
                1002,
                502,
                502,
                'PAY003'
            );
        """
    for i in range(10000):
        # print(sql)
        log.info(sql.format(i))
