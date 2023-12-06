# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/5/10'

import sys

sys.path.append('../')
import pytest
from tins.common.allureHandler import allure
from tins.common import wechat


def run():
    print("start test.....")
    try:
        pytest.main([
            "-q", "-s", "D:/oula/testcases/高危命令",
            # "-q", "-s", "/Users/zhuyixun/Downloads/oula/testcases",
            # "--reruns=1", "--reruns-delay=1",
            "-s", "-q", "--alluredir", "report/result"
        ])
        wechat.send_message_all(u"自动化测试执行完毕，测试报告请点击")
    except:
        pass
    finally:
        allure().execute_command()
    print("Test done!")


if __name__ == "__main__":
    run()
