# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
import json
import requests
from tins.config import *
from tins.api.db_sql import *
from tins.api.db_connection_info import *
from tins.api.db_manage import general_set
from tins.api.db_manage.access_set import high_risk_resources
from tins.api.high_risk_resources_data import oracle_connection_sql
from tins.api.high_risk_resources_data import permission_data
from tins.api.high_risk_resources_data import *
from tins.api import notice
from tins.api.flow import apply_flow

username = "gaowei"
_v = permission_data["PostGreSQL"]
# ##########测试数据###########
_connection = "xyz_test6666_PostgreSQL"
_database = "salespdb"
_pgUser = "GAOWEI_SCHEMA"
_table = "BIAO3333"
_column = "a"

operations = ["Delete", "Create_table", "Insert", "Update", "Alter"]
_connection_permission = operations
_database_permission = operations
_oracleUser_permission = operations
_tableGroup_permission = operations
_table_permission = operations


# _column_permission = _v["column"]


def test_001_connection():
    """
    连接名称校验
    :return:
    数据源：pg
    用例一：
    1、数据源连接下，不设置任何高危
    2、普通用户执行（insert,updata,delete,creat_table），不报高危提示。（前提：此用户有这么命令的权限）
    用例二：
    1、自定义数据源连接-高危（insert,updata,delete,creat_table），并关闭高危复核方式
    2、普通用户执行（insert,updata,delete,creat_table），报高危提示，但不报高危复核提示
    用例三：
    1、自定义数据源连接-高危（insert,updata,delete,creat_table），并开启高危复核方式
    2、普通用户执行（insert,updata,delete,creat_table），报高危提示，也提示高危复核提示
    3、此时此用户进行高危提权（insert,updata,delete,creat_table），断言可以执行通过

    用例：
    1、只自定义数据源连接-高危（insert）
    2、普通用户执行insert报高危提示，但是执行：updata,delete,creat_table）不会报高危提示
    """
    _sql_list = list(pg_connection_sql.values())
    # 清除环境，没有添加任何高危权限设置时，执行对应权限SQL语句，可以执行，不会有高危提示
    high_risk_resources.delete_all_high_risk_source_permission(_connection)
    for i in _sql_list:
        res = db_sql.run_sql_pg(_connection, i, _database, _pgUser, username)
        assert "成功" in res
    # 通用配置中，关闭高危复核方式，添加高危权限设置，执行对应权限SQL语句，有高危提示，没有复核提示
    high_risk_resources.add_high_risk_source_permission_yes_database(_connection_permission, _connection, _database)
    general_set.high_risk_review_settings(_connection)
    for i in _sql_list:
        res = db_sql.run_sql_pg(_connection, i, _database, _pgUser, username)
        assert "语句中存在对高危资源操作" in res and "OTP" not in res
    # 通用配置中，开启OTP高危复核方式，并添加高危权限设置，执行对应权限SQL语句，有高危提示，也有复核提示
    high_risk_resources.add_high_risk_source_permission_yes_database(_connection_permission, _connection, _database)
    general_set.high_risk_review_settings(_connection, 1)
    for i in _sql_list:
        res = db_sql.run_sql_pg(_connection, i, _database, _pgUser, username)
        assert "语句中存在对高危资源操作" in res and "OTP" in res


def test_002_username_apply_permission():
    """
    # 普通用户高危提权成功
    此时此用户进行高危提权（insert,updata,delete,creat_table）成功，断言可以执行通过
    :return:
    """
    _sql_list = list(pg_connection_sql.values())
    _info = apply_flow.high_risk_flow(_connection, username)
    _info = json.loads(_info)
    _id = _info["data"]
    notice.flow_audit(_id, "yes")
    for i in _sql_list:
        res = db_sql.run_sql_pg(_connection, i, _database, _pgUser, username)
        assert "语句中存在对高危资源操作" not in res


def test_003_only_apply_one_permission():
    """
    # 用例：
    # 1、只自定义数据源连接 - 高危（insert）
    # 2、普通用户执行insert报高危提示，但是执行：updata, delete, creat_table）不会报高危提示
    # 清除环境，没有添加任何高危权限设置时，执行对应权限SQL语句，可以执行，不会有高危提示
    :return:
    """
    _sql_list = list(oracle_connection_sql.values())
    high_risk_resources.delete_all_high_risk_source_permission(_connection)
    high_risk_resources.add_high_risk_source_permission_yes_database(["Insert"], _connection)
    for i in _sql_list:
        if "insert" in i.lower():
            res = db_sql.run_sql_pg(_connection, i, _database, _pgUser, username)
            assert "语句中存在对高危资源操作" in res
        else:
            res = db_sql.run_sql_pg(_connection, i, _database, _pgUser, username)
            assert "语句中存在对高危资源操作" not in res


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
