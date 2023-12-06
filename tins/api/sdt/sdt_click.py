# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/12/20'

import json
import jsonpath
from tins.api import public
from tins.api.public import *
from tins import config
import requests
import time

tabkey = time.time()


def sdt_connection_right_click(connection_name="", username="enmoadmin"):
    """
    右键连接名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/menus".format(base_url)
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "connection",
        "nodeName": connection_name,
        "nodePath": "/root/{}".format(str(connection_id)),
        "userId": username
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_schema_right_click(connection_name="", schema_name="", username="enmoadmin"):
    """
    右键schema名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/menus".format(base_url)
    if connection_type == "Oracle":
        node_type = "oracleUser"
    elif connection_type == "MySQL":
        node_type = "database"
    elif connection_type == "DamengDB":
        node_type = "schema"
    elif connection_type == "DB2":
        node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": node_type,
        "nodeName": schema_name,
        "nodePath": "/root/{}/{}".format(str(connection_id), schema_name),
        "userId": username
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_database_schema_right_click(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                    username="enmoadmin"):
    """
    右键schema名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/menus".format(base_url)
    if connection_type == "OracleCDB":
        node_type = "oracleUser"
    elif connection_type == "SQLServer":
        node_type = "schema"
    elif connection_type == "PostgreSQL":
        node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": node_type,
        "nodeName": schema_name,
        "nodePath": "/root/{}/{}/{}".format(str(connection_id), database_name, schema_name),
        "userId": username
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_schema(connection_name="", schema_name="", username="enmoadmin"):
    """
    打开schema名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    if connection_type == "Oracle":
        node_type = "oracleUser"
    if connection_type == "OracleCDB":
        node_type = "oracleUser"
    elif connection_type == "MySQL":
        node_type = "database"
    elif connection_type == "DamengDB":
        node_type = "schema"
    elif connection_type == "DB2":
        node_type = "schema"
    elif connection_type == "SQLServer":
        node_type = "schema"
    elif connection_type == "PostgreSQL":
        node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": node_type,
        "nodeName": schema_name,
        "nodePath": "/root/{}/{}".format(str(connection_id), schema_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_database(connection_name="", database_name="SALESPDB", username="enmoadmin"):
    """
    打开database名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    if connection_type == "OracleCDB":
        node_type = "database"
        _database_name = database_name
    elif connection_type == "DamengDB":
        node_type = "schema"
    elif connection_type == "DB2":
        node_type = "schema"
    elif connection_type == "SQLServer":
        node_type = "database"
        _database_name = database_name
    elif connection_type == "PostgreSQL":
        node_type = "database"
        _database_name = database_name.lower()
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": node_type,
        "nodeName": _database_name,
        "nodePath": "/root/{}/{}".format(str(connection_id), _database_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_database_schema(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                             username="enmoadmin"):
    """
    打开schema名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    if connection_type == "OracleCDB":
        node_type = "oracleUser"
    elif connection_type == "SQLServer":
        node_type = "schema"
    elif connection_type == "PostgreSQL":
        node_type = "schema"
        database_name = "salespdb"
    elif connection_type == "MogDB":
        node_type = "schema"
        database_name = "postgres"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": node_type,
        "nodeName": schema_name,
        "nodePath": "/root/{}/{}/{}".format(str(connection_id), database_name, schema_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_schema_table_group_right_click(connection_name="", schema_name="TB_SCHEMA", username="enmoadmin"):
    """
    右键表
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/menus".format(base_url)
    # if connection_type == "Oracle":
    #     node_type = "oracleUser"
    # elif connection_type == "MySQL":
    #     node_type = "database"
    # elif connection_type == "DamengDB":
    #     node_type = "schema"
    # elif connection_type == "DB2":
    #     node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "tableGroup",
        "nodeName": "表",
        "nodePath": "/root/{}/{}/表".format(str(connection_id), schema_name),
        "nodePermissionLimits": [],
        "userId": username
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_database_schema_table_group_right_click(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                                username="enmoadmin"):
    """
    右键表
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/menus".format(base_url)
    # if connection_type == "OracleCDB":
    #     node_type = "oracleUser"
    # elif connection_type == "SQLServer":
    #     node_type = "schema"
    # elif connection_type == "PostgreSQL":
    #     node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "tableGroup",
        "nodeName": "表",
        "nodePath": "/root/{}/{}/{}/表".format(str(connection_id), database_name, schema_name),
        "nodePermissionLimits": [],
        "userId": username
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_schema_table_group(connection_name="", schema_name="TB_SCHEMA", username="enmoadmin"):
    """
    打开表组
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    # if connection_type == "Oracle":
    #     node_type = "oracleUser"
    # elif connection_type == "MySQL":
    #     node_type = "database"
    # elif connection_type == "DamengDB":
    #     node_type = "schema"
    # elif connection_type == "DB2":
    #     node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "tableGroup",
        "nodeName": "表",
        "nodePath": "/root/{}/{}/表".format(str(connection_id), schema_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_database_schema_table_group(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                         username="enmoadmin"):
    """
    打开表组
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    if connection_type == "PostgreSQL":
        database_name = database_name.lower()
    # elif connection_type == "SQLServer":
    #     node_type = "schema"
    # elif connection_type == "PostgreSQL":
    #     node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "tableGroup",
        "nodeName": "表",
        "nodePath": "/root/{}/{}/{}/表".format(str(connection_id), database_name, schema_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_create_table(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                 username="enmoadmin"):
    """
    SDT下右键创建表
    :param connection_name:
    :param database_name:
    :param schema_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/statement/executeMenuActionSql".format(config.base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        database_name = schema_name
        __sql = 'CREATE TABLE "{}"."table_zyx{}" ("a" CHAR(22))'.format(schema_name, random.randint(10000, 99999))
    elif "oraclecdb" in connection_type.lower():
        __sql = 'CREATE TABLE "{}"."table_zyx{}" ("a" CHAR(22))'.format(schema_name, random.randint(10000, 99999))
    elif "mysql" in connection_type.lower():
        database_name = schema_name
        __sql = "CREATE TABLE `TB_SCHEMA111`.`qqqqq` (\n `a` char(22) \n);\n"
    elif "sqlserver" in connection_type.lower():
        __sql = 'CREATE TABLE "{}"."table_zyx{}" ("a" CHAR(22))'.format(schema_name, random.randint(10000, 99999))
    elif "postgresql" in connection_type.lower():
        __sql = 'CREATE TABLE "{}"."table_zyx{}" ("a" CHAR(22))'.format(schema_name, random.randint(10000, 99999))
        database_name = database_name.lower()
    payload = {
        "connectionId": connection_id,
        "dataSourceType": connection_type,
        "databaseName": database_name,
        "operatingDatabase": schema_name,
        "operatingObject": schema_name,
        "tabKey": tabkey,
        "statements": [
            __sql
        ]
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_preview(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                            username="enmoadmin"):
    """
    SDT下右键预览
    :param connection_name:
    :param database_name:
    :param schema_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    # connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/menu/createTable/generateSql".format(config.base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        database_name = schema_name
    payload = {
        "connectionType": connection_type,
        "schemaName": schema_name,
        "databaseName": database_name,
        "tableName": "table_zyx{}".format(random.randint(1000, 9999)),
        "primaryKeys": [],
        "columns": [
            {
                "columnName": "a",
                "dataType": "CHAR",
                "length": 22
            }
        ]
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_schema_table(connection_name="", schema_name="TB_SCHEMA", table_name="TB_TABLE", username="enmoadmin"):
    """
    打开具体表
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    # if connection_type == "Oracle":
    #     node_type = "oracleUser"
    # elif connection_type == "MySQL":
    #     node_type = "database"
    # elif connection_type == "DamengDB":
    #     node_type = "schema"
    # elif connection_type == "DB2":
    #     node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "table",
        "nodeName": table_name,
        "nodePath": "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_open_database_schema_table(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                   table_name="TB_TABLE", username="enmoadmin"):
    """
    打开具体表
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    if connection_type == "PostgreSQL":
        database_name = database_name.lower()
    # elif connection_type == "SQLServer":
    #     node_type = "schema"
    # elif connection_type == "PostgreSQL":
    #     node_type = "schema"
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "table",
        "nodeName": table_name,
        "nodePath": "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


################################################################
# 表的操作
################################################################
def sdt_table_right_click(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA", table_name="TB_TABLE",
                          username="enmoadmin"):
    """
    右键具体表名称
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/menus".format(base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "oraclecdb" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "mysql" in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "sqlserver" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "postgresql" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
        database_name = database_name.lower()
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "table",
        "nodeName": table_name,
        "nodePath": nodePath,
        "userId": username
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_open_table(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                               table_name="TB_TABLE",
                               username="enmoadmin"):
    """
    SDT下右键打开表
    :param connection_name:
    :param database_name:
    :param schema_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/menu/open".format(config.base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "mysql" in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "oraclecdb" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "sqlserver" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "postgresql" in connection_type.lower():
        database_name = database_name.lower()
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    payload = {
        "connectionId": connection_id,
        "dataSourceType": connection_type,
        "nodeName": table_name,
        "nodePath": nodePath,
        "nodeType": "table"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_design_table(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                 table_name="TB_TABLE",
                                 username="enmoadmin"):
    """
    SDT下右键设计表
    :param connection_name:
    :param database_name:
    :param schema_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/table/structure".format(config.base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "mysql" in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "oraclecdb" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "sqlserver" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "postgresql" in connection_type.lower():
        database_name = database_name.lower()
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)

    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeName": table_name,
        "nodePath": nodePath,
        "nodeType": "table"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_look_table(connection_name="", schema_name="TB_SCHEMA", table_name="TB_TABLE",
                               username="enmoadmin"):
    """
    SDT下右键查看表结构
    :param connection_name:
    :param database_name:
    :param schema_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/table/structure".format(config.base_url)
    payload = {
        "connectionId": connection_id,
        "dataSourceType": connection_type,
        "nodeName": table_name,
        "nodePath": "/root/{}/{}/表/{}".format(connection_id, schema_name, table_name),
        "nodeType": "table"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_table_rename(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                 new_table_name="TB_TABLE1",
                                 old_table_name="TB_TABLE", username="enmoadmin"):
    """
    重命名表名
    :param old_folder:
    :param new_folder:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/menu/rename".format(base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, old_table_name)
    elif "mysql" in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, old_table_name)
    elif "oraclecdb" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, old_table_name)
    elif "sqlserver" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, old_table_name)
    elif "postgresql" in connection_type.lower():
        database_name = database_name.lower()
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, old_table_name)

    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeName": new_table_name,
        "nodePath": nodePath,
        "nodeType": "table"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_table_export(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                 table_name="TB_TABLE",
                                 username="enmoadmin"):
    """
    表右键导出
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/export/export/menu".format(base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "mysql" in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "oraclecdb" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    payload = {
        "dumpType": "DUMPDATAANDSTRUCTURE",
        "fileName": "hehe1",
        "exportDataNum": 500,
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeName": table_name,
        "nodeType": "table",
        "nodePath": nodePath,
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def sdt_right_click_table_import(connection_name="", database_name="SALESPDB", schema_name="TB_SCHEMA",
                                 table_name="TB_TABLE",
                                 username="enmoadmin"):
    """
    表的右键导入
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/taskCenter/importer/importTask".format(base_url)
    if "oracle" in connection_type.lower() and "cdb" not in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "mysql" in connection_type.lower():
        nodePath = "/root/{}/{}/表/{}".format(str(connection_id), schema_name, table_name)
    elif "oraclecdb" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "sqlserver" in connection_type.lower():
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)
    elif "postgresql" in connection_type.lower():
        database_name = database_name.lower()
        nodePath = "/root/{}/{}/{}/表/{}".format(str(connection_id), database_name, schema_name, table_name)

    # payload = {
    #     # "charsetName": "UTF-8",
    #     "columnMap": [
    #         {
    #             "columnName": "a",
    #             "columnTypeName": "CHAR",
    #             "index": "0"
    #         }
    #     ],
    #     "dataStartLine": 2,
    #     "dateDelimiter": "/",
    #     "dateSort": "DMY",
    #     "dateTimeSort": "DATE TIME",
    #     "decimalPointSymbol": ".",
    #     "delimiter": ",",
    #     "fieldNameLine": 1,
    #     "filePath": "/testcase.xlsx",
    #     "fileType": "xlsx",
    #     "lineBreak": "\r\n",
    #     "timeDelimiter": ":",
    #     "connectionName": connection_name,
    #     "connectionId": connection_id,
    #     "dataSourceType": connection_type,
    #     "nodePath": nodePath,
    #     "tableName": table_name
    # }
    # payload = json.dumps(payload, ensure_ascii=False, indent=4)
    payload = {
        "columnMap": [
            {
                "columnName": "a",
                "columnTypeName": "CHAR",
                "index": "0"
            }
        ],
        "dataStartLine": 2,
        "dateDelimiter": "/",
        "dateSort": "DMY",
        "dateTimeSort": "DATE TIME",
        "decimalPointSymbol": ".",
        "delimiter": ",",
        "fieldNameLine": 1,
        "filePath": "/testcase.xlsx",
        "fileType": "xlsx",
        "lineBreak": "\r\n",
        "timeDelimiter": ":",
        "connectionName": connection_name,
        "connectionId": connection_id,
        "dataSourceType": connection_type,
        "nodePath": nodePath,
        "tableName": table_name
    }
    payload = json.dumps(payload)
    print(type(payload), payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


################################################################
# SDT文件的操作
################################################################
def sdt_folder_right_click(folder_name="", username="enmoadmin"):
    """
    右键文件夹名称
    :param folder_name:
    :param username:
    :return:
    """
    url = "{}/dms/meta/menus".format(base_url)
    payload = {
        "connectionId": 0,
        "nodeType": "connectionGroup",
        "nodeName": folder_name,
        "nodePath": "/root/g-{}".format(public.get_group_id(folder_name)),
        "nodePermissionLimits": []
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def get_sdt_connection_info(connection_name="", username="enmoadmin"):
    """
    获取数据源连接名称下的全部信息
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/dms/meta/node".format(base_url)
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "connection",
        "nodeName": connection_name,
        "nodePath": "/root/{}".format(str(connection_id))
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def switch_mode(_theme="dark", username="enmoadmin"):
    """
    切换模式
    :param _theme:
    :param username:
    :return:
    """
    url = "{}/user/users/settings".format(base_url)
    payload = {
        "theme": _theme
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def new_folder(folder="", username="enmoadmin"):
    """
    新建文件夹
    :param folder:
    :param username:
    :return:
    """
    _folder = "中文{}".format(random.randint(10000, 99999)) if folder == "" else folder
    url = "{}/dms/menu/group/0/{}".format(base_url, _folder)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers)
    if "成功" in response.text:
        return _folder
    else:
        return response.text


def new_son_folder(folder, son_folder="", username="enmoadmin"):
    """
    新建子文件夹
    :param folder:
    :param username:
    :return:
    """
    _son_folder = folder + "{}".format(random.randint(10000, 99999)) if son_folder == "" else son_folder
    folder_group_id = get_group_id(folder)
    url = "{}/dms/menu/group/{}/{}".format(base_url, folder_group_id, _son_folder)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers)
    if "成功" in response.text:
        return _son_folder
    else:
        return response.text


def rename_folder(old_folder, new_folder, username="enmoadmin"):
    """
    重命名文件夹
    :param old_folder:
    :param new_folder:
    :param username:
    :return:
    """
    url = "{}/dms/menu/rename".format(base_url)
    group_id = get_group_id(old_folder)
    payload = {
        "connectionId": 0,
        "nodeName": new_folder,
        "nodePath": "/root/g-{}".format(group_id),
        "nodeType": "connectionGroup"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if "成功" in response.text:
        return new_folder
    else:
        return response.text


def rename_connection(old_connection, new_connection, username="enmoadmin"):
    """
    重命名数据源连接名称
    :param old_connection:
    :param new_connection:
    :param username:
    :return:
    """
    connection_id = get_connection_id(old_connection)
    url = "{}/dms/menu/connect/alias/0/{}/{}".format(base_url, connection_id, new_connection)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers)
    if "成功" in response.text:
        return new_connection
    else:
        return response.text


def delete_folder(folder_name, username="enmoadmin"):
    """
    删除SDT文件夹名称
    :param folder_name:
    :param username:
    :return:
    """
    group_id = public.get_group_id(folder_name)
    url = "{}/dms/menu/group/{}".format(base_url, group_id)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers)
    return response.text


def delete_son_folder(folder_name, son_folder_name, username="enmoadmin"):
    """
    删除SDT文件夹的子文件夹名称
    :param folder_name:
    :param username:
    :return:
    """
    son_group_id = public.get_son_group_id(folder_name, son_folder_name)
    url = "{}/dms/menu/group/{}".format(base_url, son_group_id)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers)
    return response.text


def delete_all_folders(username="enmoadmin", _folder_name="中文"):
    """
    删除SDT所有名称为"中文XXX"的文件夹
    :param folder_name:
    :param username:
    :return:
    """
    all_db_connection_name = public.get_all_db_connection_name()
    for i in all_db_connection_name:
        if _folder_name in i:
            delete_all_son_folders(i, username, _folder_name)
            delete_folder(i, username)


def delete_all_son_folders(folder_name, username="enmoadmin", _folder_name="中文"):
    """
    删除父文件夹所有名称为"中文XXX"的子文件夹
    :param folder_name:
    :param username:
    :return:
    """
    _son_folder_name_list = public.get_son_folder_name_list(folder_name)
    for i in _son_folder_name_list:
        if _folder_name in i:
            delete_son_folder(folder_name, i, username)


def connection_pool(connection_name, _type=0, usernane="enmoadmin"):
    """
    连接池操作
    :param connection_name:
    :param _type:
    :param usernane:
    :return:
    """
    __type = "UPDATE" if int(_type) == 0 else "DELETE"
    url = "{}/dms/connection/reset_connection_pool".format(base_url)
    connection_id = get_connection_id(connection_name)
    payload = {
        "connectionId": connection_id,
        "type": __type
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(usernane),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == "__main__":
    # sdt_connection_right_click("zyx_test3866_SqlServer")
    # new_folder()
    # print(rename_connection("zyx_test9473_oracle", "zyx_test9473_oracle4"))
    # print(sdt_open_database_schema("zyx_test5818_oracle"))
    # print(sdt_schema_right_click("zyx_test4406_MongoDB", "admin"))
    # print(sdt_database_schema_right_click("zyx_test2489_oracleCDB"))
    # print(sdt_schema_right_click("zyx_test3083_DB2", "TB_SCHEMA"))
    # print(sdt_right_click_table_rename("zyx_test9011_SqlServer", "SALESPDB", "TB_SCHEMA", "TB_TABLE1221", "TB_TABLE"))
    payload = {"a": "中文"}
    payload = json.dumps(payload, ensure_ascii=False)

    print(type(payload), payload)
