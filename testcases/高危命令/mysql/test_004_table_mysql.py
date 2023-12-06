# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.db_connection_info import *
from tins.api.db_manage import general_set
from tins.api.db_manage.access_set import high_risk_resources
from tins.api.high_risk_resources_data import *
from tins.api import notice
from tins.api.flow import apply_flow


username = "gaowei"
_v = permission_data["MySQL"]
# ##########测试数据###########
_connection = "xyz_test6666_mysql"
_mysqlUser = "GAOWEI_SCHEMA"
_table = "BIAO3333"
_column = "a"

operations = ["Delete", "Create_table", "Insert", "Update", "Alter"]
_connection_permission = operations
_mysqlUser_permission = operations
_tableGroup_permission = operations
_table_permission = operations


def test_001_table():
    """
    :return:
    """
    _sql_list = list(mysql_table_sql.values())
    # 清除环境，没有添加任何高危权限设置时，执行对应权限SQL语句，可以执行，不会有高危提示
    high_risk_resources.delete_all_high_risk_source_permission(_connection)
    for i in _sql_list:
        res = db_sql.run_sql_mysql(_connection, i, _mysqlUser, username)
        assert "成功" in res
    # 通用配置中，关闭高危复核方式，添加高危权限设置，执行对应权限SQL语句，有高危提示，没有复核提示
    high_risk_resources.add_high_risk_source_permission_no_database(_table_permission, _connection, _mysqlUser, "表", _table)
    general_set.high_risk_review_settings(_connection)
    for i in _sql_list:
        res = db_sql.run_sql_mysql(_connection, i, _mysqlUser, username)
        assert "语句中存在对高危资源操作" in res and "OTP" not in res
    # 通用配置中，开启TP高危复核方式，并添加高危权限设置，执行对应权限SQL语句，有高危提示，也有复核提示
    high_risk_resources.add_high_risk_source_permission_no_database(_table_permission, _connection, _mysqlUser, "表", _table)
    general_set.high_risk_review_settings(_connection, 1)
    for i in _sql_list:
        res = db_sql.run_sql_mysql(_connection, i, _mysqlUser, username)
        assert "语句中存在对高危资源操作" in res and "OTP" in res


def test_002_username_apply_permission():
    """
    # 普通用户高危提权成功
    此时此用户进行高危提权（insert,updata,delete,creat_table）成功，断言可以执行通过
    :return:
    """
    _sql_list = list(mysql_table_sql.values())
    _info = apply_flow.high_risk_flow(_connection, username)
    _info = json.loads(_info)
    _id = _info["data"]
    notice.flow_audit(_id, "yes")
    for i in _sql_list:
        res = db_sql.run_sql_mysql(_connection, i, "", username)
        assert "语句中存在对高危资源操作" not in res


def test_003_only_apply_one_permission():
    """
    # 用例：
    # 1、只自定义数据源连接 - 高危（insert）
    # 2、普通用户执行insert报高危提示，但是执行：updata, delete, creat_table）不会报高危提示
    # 清除环境，没有添加任何高危权限设置时，执行对应权限SQL语句，可以执行，不会有高危提示
    :return:
    """
    _sql_list = list(mysql_connection_sql.values())
    high_risk_resources.delete_all_high_risk_source_permission(_connection)
    high_risk_resources.add_high_risk_source_permission_no_database(["Insert"], _connection, _mysqlUser, "表", _table)
    for i in _sql_list:
        if "insert" in i.lower():
            res = db_sql.run_sql_mysql(_connection, i, _mysqlUser, username)
            assert "语句中存在对高危资源操作" in res
        else:
            res = db_sql.run_sql_mysql(_connection, i, _mysqlUser, username)
            assert "语句中存在对高危资源操作" not in res


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
