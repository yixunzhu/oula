# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/7/26'

import pytest
import json
from tins.api.audit import caozuo_audit


def test_001_home_page():
    """
    判断首页正常访问
    :param:
    :return:
    """
    assert caozuo_audit.home_page() == 200


def test_002_all_operate_type():
    """
    过滤条件：事件类型
    :return:
    """
    res = caozuo_audit.all_operate_type()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


def test_003_detail():
    """
    过滤条件：查询
    :return:
    """
    res = caozuo_audit.detail()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


def test_004_simple_users():
    """
    过滤条件：用户
    :return:
    """
    res = caozuo_audit.simple_users()
    res_json = json.loads(res)
    assert "成功" in res
    assert len(res_json["data"]) > 0


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
