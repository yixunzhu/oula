# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
import random
from tins.api import public
from tins.api import db_connection_info


def test_001_right_connection(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    右键数据源连接
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection()
    for i in connection_name_list:
        res = sdt_click.sdt_connection_right_click(i)
        res = json.loads(res)
        _menu_name_list = jsonpath.jsonpath(res, "$.data..menuName")
        _valid_list = jsonpath.jsonpath(res, "$.data..valid")
        new_menu_name_list = []
        for ii, iii in zip(_valid_list, _menu_name_list):
            if ii:
                new_menu_name_list.append(iii)
        _data_type = public.get_data_type(i)
        print(i)
        assert set(db_connection_info.db_connections_right_click_info[_data_type]) == set(new_menu_name_list)
    # print(_valid_list)
    # print("diyi", _menu_name_list)
    # for iii in _menu_name_list:
    #     bbb = jsonpath.jsonpath(res, "$.data[?(@.menuName=='{}')].valid".format(iii))
    #     print(type(bbb), bbb)
    #     if type(bbb) is list:
    #         if False in bbb:
    #             print("111:", iii)
    #             _menu_name_list.remove(iii)
    #     else:
    #         if bbb:
    #             print("222:", iii)
    #             _menu_name_list.remove(iii)
    # _data_type = public.get_data_type("zyx_test6278_DB2")
    # # print("vvv:", i, res)
    # if set(db_connection_info.db_connections_right_click_info[_data_type]) == set(_menu_name_list):
    #     pass
    # else:
    #     print("zyx_test6278_DB2", _menu_name_list)
    #     # assert set(db_connection_info.db_connections_right_click_info[_data_type]) == set(_menu_name_list)


def test_002_rename_connection(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    重命名连接名
    :return:
    """
    fixture_delete_all_db_connection()
    _random = random.randint(1000, 9999)
    _connection_name_list = fixture_create_all_db_connection()
    _new_connection_name_list = []
    for i in _connection_name_list:
        _new_connection_name_list.append(sdt_click.rename_connection(i, i + str(_random)))
    a = str(public.get_info())
    for i in _new_connection_name_list:
        assert i in a


def test_003_connection_pool(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    重置连接池/回收连接池
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    for i in db_connection_list:
        for ii in range(0, 2):
            res = sdt_click.connection_pool(i)
            assert "成功" in res


def test_004_right_connection_refresh(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    右键连接名称-刷新
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    for i in db_connection_list:
        res = sdt_click.get_sdt_connection_info(i)
        assert "成功" in res


def test_005_refresh(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    刷新
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    _info = public.get_info()
    for i in db_connection_list:
        assert i in str(_info)
        assert "成功" in str(_info)


def test_006_unauthorized_info():
    """
    展开未授权组
    :return:
    """
    _info = public.get_unauthorized_info()
    assert "成功" in str(_info)


def test_007_open_sdt(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    打开所有数据源的SDT,断言SDT能否打开，是否有数据
    :param fixture_create_all_db_connection:
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection()
    for i in connection_name_list:
        _open_sdt_info = sdt_click.get_sdt_connection_info(i)
        assert '"resCode":10000,"resMsg":"成功","data":{"resourceLimit":false,"data":[{"connectionId"' in _open_sdt_info


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
