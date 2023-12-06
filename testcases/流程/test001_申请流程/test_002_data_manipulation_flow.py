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


def test_001_data_manipulation_flow(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    数据操作提权
    步骤：
    1、管理员新建数据源连接,此时断言新用户A申请数据操作提权，界面中无数据源连接
    2、管理员在后台设置普通用户A可以访问
    3、普通用户A此时进行操作权限，断言无权限，需要提权
    4、此时普通用户A进行申请数据操作提权
    5、对应审核员审核拒绝，断言无权限，需要提权

    重复步骤：
    1、此时普通用户A进行申请数据操作提权
    2、对应审核员审核通过，断言有权限
    :param fixture_create_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    # db_connection_list = _data(fixture_create_all_db_connection, fixture_delete_all_db_connection)[0]
    # username = _data(fixture_create_all_db_connection, fixture_delete_all_db_connection)[1]
    # 新用户A申请数据操作提权，界面中无数据源连接
    _ui_info = apply_flow.get_flow_ui_info(2, username)
    assert '"data":[]' in _ui_info
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        if "oracleCDB" in i:
            oraclecdb_res_sql_key_list = list(oraclecdb.keys())
            for ii in oraclecdb_res_sql_key_list:
                res_v = run_sql_oracleCDB(i, oraclecdb[ii], username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "oracle" in i and "oracleCDB" not in i:
            oracle_res_sql_key_list = list(oracle.keys())
            for ii in oracle_res_sql_key_list:
                res_v = run_sql_oracle(i, oracle[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "mysql" in i:
            mysql_res_sql_key_list = list(mysql.keys())
            for ii in mysql_res_sql_key_list:
                res_v = run_sql_mysql(i, mysql[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "SqlServer" in i:
            sqlserver_res_sql_key_list = list(sqlserver.keys())
            for ii in sqlserver_res_sql_key_list:
                res_v = run_sql_sqlserver(i, sqlserver[ii], "SALESPDB", username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "PostgreSQL" in i:
            pg_res_sql_key_list = list(pg.keys())
            for ii in pg_res_sql_key_list:
                res_v = run_sql_pg(i, pg[ii], "salespdb", "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
    public.delete_username(username)


def test_002_jujue(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    :param fixture_create_all_db_connection:
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # 此时普通用户A进行申请数据操作提权
        _info = apply_flow.data_manipulation_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员先进行审批拒绝
        notice.flow_audit(_id, "no")
        if "oracleCDB" in i:
            oraclecdb_res_sql_key_list = list(oraclecdb.keys())
            for ii in oraclecdb_res_sql_key_list:
                res_v = run_sql_oracleCDB(i, oraclecdb[ii], username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "oracle" in i and "oracleCDB" not in i:
            oracle_res_sql_key_list = list(oracle.keys())
            for ii in oracle_res_sql_key_list:
                res_v = run_sql_oracle(i, oracle[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "mysql" in i:
            mysql_res_sql_key_list = list(mysql.keys())
            for ii in mysql_res_sql_key_list:
                res_v = run_sql_mysql(i, mysql[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "SqlServer" in i:
            sqlserver_res_sql_key_list = list(sqlserver.keys())
            for ii in sqlserver_res_sql_key_list:
                res_v = run_sql_sqlserver(i, sqlserver[ii], "SALESPDB", username)
                assert "权限校验失败，请查看执行日志" in res_v
        elif "PostgreSQL" in i:
            pg_res_sql_key_list = list(pg.keys())
            for ii in pg_res_sql_key_list:
                res_v = run_sql_pg(i, pg[ii], "salespdb", "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
    public.delete_username(username)


def test_003_pass(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    :param fixture_create_all_db_connection:
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # 此时普通用户A再次进行申请数据操作提权
        _info = apply_flow.data_manipulation_flow(i, username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批进行审批通过
        notice.flow_audit(_id, "yes")
        if "oracleCDB" in i:
            oraclecdb_res_sql_key_list = list(oraclecdb.keys())
            for ii in oraclecdb_res_sql_key_list:
                res_v = run_sql_oracleCDB(i, oraclecdb[ii], username)
                assert "权限校验失败，请查看执行日志" not in res_v
        elif "oracle" in i and "oracleCDB" not in i:
            oracle_res_sql_key_list = list(oracle.keys())
            for ii in oracle_res_sql_key_list:
                res_v = run_sql_oracle(i, oracle[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" not in res_v
        elif "mysql" in i:
            mysql_res_sql_key_list = list(mysql.keys())
            for ii in mysql_res_sql_key_list:
                res_v = run_sql_mysql(i, mysql[ii], "TB_SCHEMA", username)
                print(i, username, mysql[ii])
                assert "权限校验失败，请查看执行日志" not in res_v
        elif "SqlServer" in i:
            sqlserver_res_sql_key_list = list(sqlserver.keys())
            for ii in sqlserver_res_sql_key_list:
                res_v = run_sql_sqlserver(i, sqlserver[ii], "SALESPDB", username)
                assert "权限校验失败，请查看执行日志" not in res_v
        elif "PostgreSQL" in i:
            pg_res_sql_key_list = list(pg.keys())
            for ii in pg_res_sql_key_list:
                res_v = run_sql_pg(i, pg[ii], "salespdb", "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" not in res_v
    public.delete_username(username)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
