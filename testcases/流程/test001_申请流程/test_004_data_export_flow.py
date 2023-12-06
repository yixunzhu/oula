# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.db_sql import *
from tins.api import public
from tins.api.db_manage.access_set import role_manage
from tins.api.flow import apply_flow
from tins.api import notice
from tins.data_factory.sql_data import *
from tins.api.result_collection import export


def test_001(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    数据导出提权
    步骤：
    1、管理员新建数据源连接,此时断言新用户A申请数据导出提权，界面中无数据源连接
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
    _ui_info = apply_flow.get_flow_ui_info(4, username)
    assert '"data":[]' in _ui_info
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # 此时普通用户A进行申请select提权
        _info = apply_flow.data_manipulation_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员审批通过
        notice.flow_audit(_id, "yes")
        if "oracleCDB" in i:
            res_v = export.common_export(username, oraclecdb["select"], i)
            assert '"resCode":-1' in res_v
        elif "oracle" in i and "oracleCDB" not in i:
            res_v = export.common_export(username, oracle["select"], i)
            assert '"resCode":-1' in res_v
        elif "mysql" in i:
            res_v = export.common_export(username, mysql["select"], i)
            assert '"resCode":-1' in res_v
        elif "SqlServer" in i:
            res_v = export.common_export(username, sqlserver["select"], i)
            assert '"resCode":-1' in res_v
        elif "PostgreSQL" in i:
            res_v = export.common_export(username, pg["select"], i)
            assert '"resCode":-1' in res_v
    public.delete_username(username)


def test_002(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    数据导出提权
    步骤：
    4、普通用户进行导出提权流程，管理通过后，此用户进行可以导出
    :param fixture_create_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # 此时普通用户A进行申请select提权
        _info = apply_flow.data_manipulation_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员审批通过
        notice.flow_audit(_id, "yes")

        # 此时普通用户A进行申请导出提权
        _info = apply_flow.data_export_flow(i, username, "enmoadmin")
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员审批通过
        notice.flow_audit(_id, "yes")

        if "oracleCDB" in i:
            res_v = export.common_export(username, oraclecdb["select"], i)
            assert '"resCode":10000' in res_v
        elif "oracle" in i and "oracleCDB" not in i:
            res_v = export.common_export(username, oracle["select"], i)
            assert '"resCode":10000' in res_v
        elif "mysql" in i:
            res_v = export.common_export(username, mysql["select"], i)
            assert '"resCode":10000' in res_v
        elif "SqlServer" in i:
            res_v = export.common_export(username, sqlserver["select"], i)
            assert '"resCode":10000' in res_v
        elif "PostgreSQL" in i:
            res_v = export.common_export(username, pg["select"], i)
            assert '"resCode":10000' in res_v
    public.delete_username(username)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
