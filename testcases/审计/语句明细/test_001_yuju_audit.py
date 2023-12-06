# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/7/26'

import pytest
import json
from tins.api.audit import yuju_audit


def test_001_home_page():
    """
    判断首页正常访问
    :param:
    :return:
    """
    assert yuju_audit.home_page() == 200


def test_002_toolbar():
    """
    数据源类型下拉框
    :return:
    """
    res = yuju_audit.toolbar()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


def test_003_find_audit_log():
    """
    过滤条件：查询
    :return:
    """
    res = yuju_audit.find_audit_log()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


def test_004_simple_users():
    """
    过滤条件：用户
    :return:
    """
    res = yuju_audit.simple_users()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


def test_005_find_server_ip():
    """
    过滤条件：请选择主机
    :return:
    """
    res = yuju_audit.find_server_ip()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


def test_006_datasource_list():
    """
    过滤条件：数据源类型
    :return:
    """
    res = yuju_audit.datasource_list()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
