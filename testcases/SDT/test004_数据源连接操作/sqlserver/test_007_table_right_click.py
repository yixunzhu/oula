# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
from tins.api import db_sql
import random


def test_001_table_right_click(fixture_delete_all_db_connection):
    """
    右键表
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("sqlserver")
    res = sdt_click.sdt_table_right_click(_db_connection)
    assert '"resCode":10000,"resMsg":"成功"' in res
    res = json.loads(res)
    _data = jsonpath.jsonpath(res, "$.data..menuName")
    _list = ['打开表', '查看表结构', '重命名', '添加表', '设计表', '复制', '文本导入', '刷新', '导出提权', '脱敏提权']
    assert set(_list) == set(_data)


def test_002_right_click_open_table(fixture_delete_all_db_connection):
    """
    右键打开表
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("sqlserver")
    res = sdt_click.sdt_right_click_open_table(_db_connection)
    assert '"resCode":10000,"resMsg":"成功"' in res
    assert 'SELECT * FROM' in res


def test_003_right_click_design_table(fixture_delete_all_db_connection):
    """
    右键设计表
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("sqlserver")
    res = sdt_click.sdt_right_click_design_table(_db_connection)
    assert '"resCode":10000,"resMsg":"成功"' in res


def test_004_right_click_table_rename(fixture_delete_all_db_connection):
    """
    右键表重命名
    :param fixture_delete_all_db_connection:
    :return:
    """
    _random = random.randint(1000, 9999)
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("sqlserver")
    _sql = 'CREATE TABLE [TB_SCHEMA].[TB_TABLE] (a char(22),b char(22))'
    db_sql.run_sql_sqlserver(_db_connection, _sql)
    new_table_name = "TB_TABLE{}".format(str(_random))
    old_table_name = "TB_TABLE"
    sdt_click.sdt_open_database(_db_connection)
    res = sdt_click.sdt_right_click_table_rename(_db_connection, "SALESPDB", "TB_SCHEMA", new_table_name, old_table_name)
    sdt_click.sdt_right_click_table_rename(_db_connection, "SALESPDB", "TB_SCHEMA", old_table_name, new_table_name)
    assert '"resCode":10000,"resMsg":"成功"' in res


def test_005_sdt_right_click_table_import(fixture_delete_all_db_connection):
    """
    右键表导入
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("sqlserver")
    res = sdt_click.sdt_right_click_table_import(_db_connection)
    assert '"resCode":10000,"resMsg":"成功"' in res


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
