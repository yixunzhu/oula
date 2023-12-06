# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
import json
import requests
from tins.config import *
from tins.api.db_sql import *
from tins.api.db_connection_info import *
from tins.api.db_manage.access_set import role_manage
from tins.api.result_collection import export
from tins.data_factory.sql_data import *


def test_001_dev_model_no(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    不开启开发者模式后，校验普通用户能否拥有管理员权限
    备注：此用例目前只支持4大数据源
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection()
    username = create_username_and_update_pw()
    for i in connection_name_list:
        role_manage.initialize_role_binding_user(i, username)
    # 断言普通用户是否拥有管理员权限
    print(username)
    for i in connection_name_list:
        if "oracle" in i.lower() and "oraclecdb" not in i.lower():
            res_export = export.all_export(username, i, oracle['select'])
            oracle_res_sql_key_list = list(oracle.keys())
            for ii in oracle_res_sql_key_list:
                res_v = run_sql_oracle(i, oracle[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
            assert "成功" not in res_export
        elif "oraclecdb" in i.lower():
            res_export = export.all_export(username, i, oraclecdb['select'])
            oraclecdb_res_sql_key_list = list(oraclecdb.keys())
            for ii in oraclecdb_res_sql_key_list:
                res_v = run_sql_oracleCDB(i, oraclecdb[ii], username)
                assert "权限校验失败，请查看执行日志" in res_v
            assert "成功" not in res_export
        elif "mysql" in i.lower():
            res_export = export.all_export(username, i, mysql['select'])
            mysql_res_sql_key_list = list(mysql.keys())
            for ii in mysql_res_sql_key_list:
                res_v = run_sql_mysql(i, mysql[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
            assert "成功" not in res_export
        elif "sqlserver" in i.lower():
            res_export = export.all_export(username, i, sqlserver['select'])
            sqlserver_res_sql_key_list = list(sqlserver.keys())
            for ii in sqlserver_res_sql_key_list:
                res_v = run_sql_sqlserver(i, sqlserver[ii], "SALESPDB", username)
                assert "权限校验失败，请查看执行日志" in res_v
            assert "成功" not in res_export
        elif "postgresql" in i.lower():
            res_export = export.all_export(username, i, pg['select'])
            pg_res_sql_key_list = list(pg.keys())
            for ii in pg_res_sql_key_list:
                res_v = run_sql_pg(i, pg[ii], "salespdb", "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" in res_v
            assert "成功" not in res_export


def test_002_dev_model_yes(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    开启开发者模式后，校验普通用户能否拥有管理员权限
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection(0, 1)
    username = create_username_and_update_pw()
    for i in connection_name_list:
        role_manage.initialize_role_binding_user(i, username)
    # 断言普通用户是否拥有管理员权限
    for i in connection_name_list:
        if "oracle" in i.lower() and "oraclecdb" not in i.lower():
            res_export = export.all_export(username, i, oracle['select'])
            oracle_res_sql_key_list = list(oracle.keys())
            for ii in oracle_res_sql_key_list:
                res_v = run_sql_oracle(i, oracle[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" not in res_v
            assert "成功" in res_export
        elif "oraclecdb" in i.lower():
            res_export = export.all_export(username, i, oraclecdb['select'])
            oraclecdb_res_sql_key_list = list(oraclecdb.keys())
            for ii in oraclecdb_res_sql_key_list:
                res_v = run_sql_oracleCDB(i, oraclecdb[ii], username)
                assert "权限校验失败，请查看执行日志" not in res_v
            assert "成功" in res_export
        elif "mysql" in i.lower():
            res_export = export.all_export(username, i, mysql['select'])
            mysql_res_sql_key_list = list(mysql.keys())
            for ii in mysql_res_sql_key_list:
                res_v = run_sql_mysql(i, mysql[ii], "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" not in res_v
            assert "成功" in res_export
        elif "sqlserver" in i.lower():
            res_export = export.all_export(username, i, sqlserver['select'])
            sqlserver_res_sql_key_list = list(sqlserver.keys())
            for ii in sqlserver_res_sql_key_list:
                res_v = run_sql_sqlserver(i, sqlserver[ii], "SALESPDB", username)
                assert "权限校验失败，请查看执行日志" not in res_v
            assert "权限校验失败，请查看执行日志" not in res_export
        elif "postgresql" in i.lower():
            res_export = export.all_export(username, i, pg['select'])
            pg_res_sql_key_list = list(pg.keys())
            for ii in pg_res_sql_key_list:
                res_v = run_sql_pg(i, pg[ii], "salespdb", "TB_SCHEMA", username)
                assert "权限校验失败，请查看执行日志" not in res_v
            assert "权限校验失败，请查看执行日志" not in res_export


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
