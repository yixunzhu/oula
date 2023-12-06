# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2021/6/4'


import os
import time
import subprocess
# from .log import Logs
from tins.common.log import Logs
from tins.common import helper


class allure(object):
    log = Logs()

    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.allure_html_path = os.path.join(self.BASE_PATH, 'report', 'allure_html')
        self.result_path = os.path.join(self.BASE_PATH, 'report', 'result')
        self.ALLURE_COMMAND = 'allure generate {} -o {} --clean'.format(self.result_path, self.allure_html_path)
        print("self.ALLURE_COMMAND:", self.ALLURE_COMMAND)
        if helper.is_mac_sys():
            self.del_file = 'rm -rf {}'.format(self.result_path)
        else:
            self.del_file = 'del /F /S /Q {}'.format(self.result_path)

    def execute_command(self):
        time.sleep(1)
        try:
            subprocess.call(self.ALLURE_COMMAND, shell=True)
            subprocess.call(self.del_file, shell=True)
        except Exception as e:
            self.log.error('生成allure报告出错：%s' % (e))


if __name__ == "__main__":
    allure().execute_command()