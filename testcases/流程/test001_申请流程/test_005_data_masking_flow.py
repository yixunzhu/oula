# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest

from tins.api import notice
from tins.api.db_manage.access_set import role_manage
from tins.api.db_manage.desensitization_set import desensitization_resource
from tins.api.db_sql import *
from tins.api.flow import apply_flow
from tins.data_factory.sql_data import *


def test_001(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    数据脱敏提权流程
    步骤：
    1、管理员新建数据源连接,此时断言新用户A申请脱敏提权，界面中无数据源连接
    2、管理员在后台设置普通用户A可以访问此数据源连接，并设置成可以select
    3、此用户select后进行导出，提示无导出权限
    4、普通用户进行导出提权流程，管理通过后，此用户进行可以导出
    :param fixture_create_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    # 新用户A申请导出提权，界面中无数据源连接
    _ui_info = apply_flow.get_flow_ui_info(5, username)
    assert '"data":[]' in _ui_info
    _a = "1234567"
    _b = "abcdefg"
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # 此时普通用户A进行申请select提权
        _info = apply_flow.data_manipulation_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员审批通过
        notice.flow_audit(_id, "yes")
        # 管理员进行设置脱敏资源权限
        desensitization_resource.add_desensitization_resource(i)
        if "oracleCDB" in i:
            _info = run_sql_oracleCDB(i, oraclecdb["select_tm"], username)
            assert "*******" in _info
        elif "oracle" in i and "oracleCDB" not in i:
            _info = run_sql_oracle(i, oracle["select_tm"], "TB_SCHEMA", username)
            assert "*******" in _info
        elif "mysql" in i:
            _info = run_sql_mysql(i, mysql["select_tm"], "TB_SCHEMA", username)
            assert "*******" in _info
        elif "SqlServer" in i:
            _info = run_sql_sqlserver(i, sqlserver["select_tm"], "SALESPDB", username)
            assert "*******" in _info
        elif "PostgreSQL" in i:
            _info = run_sql_pg(i, pg["select_tm"], "salespdb", "TB_SCHEMA", username)
            assert "*******" in _info
    public.delete_username(username)


def test_002(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    数据脱敏提权流程
    步骤：
    1、管理员新建数据源连接,此时断言新用户A申请脱敏提权，界面中无数据源连接
    2、管理员在后台设置普通用户A可以访问此数据源连接，并设置成可以select
    3、此用户select后进行导出，提示无导出权限
    4、普通用户进行导出提权流程，管理通过后，此用户进行可以导出
    :param fixture_create_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    # 新用户A申请导出提权，界面中无数据源连接
    _ui_info = apply_flow.get_flow_ui_info(5, username)
    assert '"data":[]' in _ui_info
    _a = "1234567"
    _b = "abcdefg"
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # 此时普通用户A进行申请select提权
        _info = apply_flow.data_manipulation_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员审批通过
        notice.flow_audit(_id, "yes")
        # 管理员进行设置脱敏资源权限
        desensitization_resource.add_desensitization_resource(i)
        # 此时普通用户A进行申请脱敏资源提权
        _info = apply_flow.data_masking_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员审批通过
        notice.flow_audit(_id, "yes")
        if "oracleCDB" in i:
            _info = run_sql_oracleCDB(i, oraclecdb["select_tm"], username)
            assert _a in _info
        elif "oracle" in i and "oracleCDB" not in i:
            _info = run_sql_oracle(i, oracle["select_tm"], "TB_SCHEMA", username)
            assert _a in _info
        elif "mysql" in i:
            _info = run_sql_mysql(i, mysql["select_tm"], "TB_SCHEMA", username)
            assert _a in _info
        elif "SqlServer" in i:
            _info = run_sql_sqlserver(i, sqlserver["select_tm"], "SALESPDB", username)
            assert _a in _info
        elif "PostgreSQL" in i:
            _info = run_sql_pg(i, pg["select_tm"], "salespdb", "TB_SCHEMA", username)
            assert _a in _info
    public.delete_username(username)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
