# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.db_connection_info import *
from tins.api.db_sql import *


def test_001_create_dbs_connection():
    """
    校验能否创建数据源连接
    :return:
    """
    db_list = list(db_connections.keys())
    connection_name_list = []
    for i in db_list:
        connection_name = create_db_connection(i)
        if "失败" not in connection_name:
            connection_name_list.append(connection_name)
    for i in connection_name_list:
        delete_db_connection_name(i)
    v_list = ["zyx_test" in i for i in connection_name_list]
    for i in v_list:
        assert i


def test_002_is_all_dbs_connection():
    """
    校验所有的数据库连接是否可以正常连上
    :return:
    """
    _title = is_all_dbs_connection()
    print(_title)
    assert "False" not in _title


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
