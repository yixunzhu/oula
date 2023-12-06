# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/12/19'

import json
import time
from tins.api import public
from tins.api.public import *
from tins import config
import requests
from tins.api.connection_management import general_configuration
import random
from tins.api import db_connection_info
from tins.config import *

tabkey = time.time()


def get_id():
    return str(tabkey)


def common_export(username="enmoadmin", sql="", connection_name="", databaseName="SALESPDB", operatingObject="TB_SCHEMA", export_format="EXCEL", export_data_num=500):
    """
    常规导出
    5个参数
    :param username: 用户名
    :param connection_name: 数据库连接名
    :param sql: 查询的sql语句
    :param export_format: 导出格式，默认excle（CSV,TXT,PDF,SQL）
    :param export_data_num: 导出行数，默认500行
    :return:
    """
    false = False
    connection_type = get_data_type(connection_name)
    url = "{}/export/export".format(base_url)
    if connection_type == "Oracle" or connection_type == "MySQL":
        _databaseName = operatingObject
        _operatingObject = operatingObject
    elif connection_type == "OracleCDB":
        _databaseName = databaseName
        _operatingObject = operatingObject
    elif connection_type == "SQLServer":
        _databaseName = databaseName
        _operatingObject = databaseName
    elif connection_type == "PostgreSQL":
        _databaseName = databaseName.lower()
        _operatingObject = operatingObject
    payload = {
        "exportFormat": export_format.upper(),
        "fileName": get_id(),
        "exportDataNum": int(export_data_num),
        "statement": sql,
        "operatingObject": _operatingObject,
        "databaseName": _databaseName,
        "connectionId": public.get_connection_id(connection_name),
        "connectionType": connection_type,
        "resultNum": 1,
        "containTempTable": false,
        "tabKey": get_id()
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def all_export(username="enmoadmin", connection_name="", sql="", export_format="EXCEL"):
    """
    全部导出
    4个参数
    :param username: 用户名
    :param connection_name: 数据库连接名
    :param sql: 查询的sql语句
    :param export_format: 导出格式，默认excle（CSV,TXT,PDF,SQL）
    :return:
    """
    false = False
    connection_type = get_data_type(connection_name)
    url = "{}/export/export/fullExport".format(base_url)
    payload = {
        "exportFormat": export_format.upper(),
        "fileName": get_id(),
        "containTempTable": false,
        "statement": sql,
        "connectionId": public.get_connection_id(connection_name),
        "connectionType": connection_type,
        "operatingObject": "",
        "databaseName": "",
        "tabKey": get_id()
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == "__main__":
    # sql = 'SELECT * FROM "XYZ_SCHEMA_2583"."BIAO5455"'
    # res = common_export("test33990", "zyx_test8962_oracle", sql)
    # print(res)
    sql_select = 'SELECT * FROM "TB_SCHEMA"."TB_TABLE"'
    # a = common_export("test94832", "zyx_test4026_mysql", sql_select)
    # print(a)
    a = common_export("test44927", sql_select, "zyx_test4738_oracle")
    print(a)