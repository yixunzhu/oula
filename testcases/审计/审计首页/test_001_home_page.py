# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/7/26'

import pytest
import json
from tins.api.audit import home_page


def test_001_home_page():
    """
    判断首页正常访问
    :param:
    :return:
    """
    assert home_page.home_page() == 200


def test_002_sql_execute_amount():
    """
    首页数据
    :return:
    """
    res = home_page.sql_execute_amount()
    res_json = json.loads(res)
    assert res_json["data"]["allCount"] > 1
    assert res_json["data"]["errorCount"] > 1
    assert res_json["data"]["activeUserCount"] > 1


def test_003_export():
    """
    导出
    :return:
    """
    res = home_page.sql_execute_amount()
    assert "成功" in res


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
