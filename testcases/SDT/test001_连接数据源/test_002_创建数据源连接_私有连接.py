# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'


import pytest
from tins.api.db_connection_info import *


def test_001_private_connection_no(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    不勾选私有连接，校验私有连接是否生效
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection()
    username = create_username_and_update_pw()
    unauthorized_info = get_unauthorized_info(username)
    delete_username(username)
    for i in connection_name_list:
        assert i in str(unauthorized_info)


def test_002_private_connection_yes(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    勾选私有连接，校验私有连接是否生效
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection(1)
    username = create_username_and_update_pw()
    unauthorized_info = get_unauthorized_info(username)
    delete_username(username)
    for i in connection_name_list:
        assert i not in str(unauthorized_info)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
