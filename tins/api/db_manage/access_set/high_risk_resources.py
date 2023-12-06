# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/12'

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
from tins.api.db_manage import db_manage_public


# 优化添加高危权限的方法
def add_high_risk_source_permission_no_database(operations=["Select"], connection_name="", oracle_user="", table_group="",
                                           table="", column=""):
    """
    增加高危权限，默认添加数据连接的
    此方法拥有添加数据源不含database的
    :param connection_name: 连接名称
    :param operations: list元组，权限列表如:["Delete","Drop","Insert","Select","Update"]
    :return:
    """
    _operations = [i.lower().capitalize() for i in operations]
    _random = random.randint(10000, 99999)
    _operations.append(_random)
    connection_type = get_data_type(connection_name)
    _permission_name = "zyx_{}".format(_random)
    connection_id = get_connection_id(connection_name)
    # _data_type = get_data_type(connection_name)
    url = "{}/user/permission/permission".format(base_url)
    if oracle_user == "":
        obj_names = "/root/0/{}".format(connection_id)
        obj_type = "connection"
    elif oracle_user != "" and table_group == "":
        obj_names = "/root/0/{}/{}".format(connection_id, oracle_user)
        if connection_type == "Oracle":
            obj_type = "oracleUser"
        elif connection_type == "MySQL":
            obj_type = "database"
    elif oracle_user != "" and table_group != "" and table == "":
        obj_names = "/root/0/{}/{}/{}".format(connection_id, oracle_user, "表")
        obj_type = "tableGroup"
    elif oracle_user != "" and table_group != "" and table != "" and column == "":
        obj_names = "/root/0/{}/{}/{}/{}".format(connection_id, oracle_user, "表", table)
        obj_type = "table"
    elif oracle_user != "" and table_group != "" and table != "" and column != "":
        obj_names = "/root/0/{}/{}/{}/{}/列组/{}".format(connection_id, oracle_user, "表", table, column)
        obj_type = "column"
    payload = {
        "dataSourceType": connection_type,
        "permissionObject": {
            "name": _permission_name,
            "objNames": [
                obj_names
            ],
            "objType": obj_type,
            "operations": _operations,
            "permissionType": "highRiskOperation"
        },
        "permissionType": "highRiskOperation"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return _permission_name


def add_high_risk_source_permission_yes_database(operations=["Select"], connection_name="", database="", oracle_user="", table_group="",
                                           table="", column=""):
    """
    增加高危权限，默认添加数据连接的
    此方法拥有添加数据源含有database的
    :param connection_name: 连接名称
    :param operations: list元组，权限列表如:["Delete","Drop","Insert","Select","Update"]
    :return:
    """
    _operations = [i.lower().capitalize() for i in operations]
    _random = random.randint(10000, 99999)
    _operations.append(_random)
    connection_type = get_data_type(connection_name)
    _permission_name = "zyx_高危权限{}".format(_random)
    connection_id = get_connection_id(connection_name)
    # _data_type = get_data_type(connection_name)
    url = "{}/user/permission/permission".format(base_url)
    if database == "":
        obj_names = "/root/0/{}".format(connection_id)
        obj_type = "connection"
    elif database != "" and oracle_user == "":
        obj_names = "/root/0/{}/{}".format(connection_id, database)
        obj_type = "database"
    elif oracle_user != "" and table_group == "":
        obj_names = "/root/0/{}/{}/{}".format(connection_id, database, oracle_user)
        if connection_type == "OracleCDB":
            obj_type = "oracleUser"
        elif connection_type == "PostgreSQL":
            obj_type = "schema"
        elif connection_type == "SQLServer":
            obj_type = "schema"
    elif oracle_user != "" and table_group != "" and table == "":
        obj_names = "/root/0/{}/{}/{}/{}".format(connection_id, database, oracle_user, "表")
        obj_type = "tableGroup"
    elif oracle_user != "" and table_group != "" and table != "" and column == "":
        obj_names = "/root/0/{}/{}/{}/{}/{}".format(connection_id, database, oracle_user, "表", table)
        obj_type = "table"
    payload = {
        "dataSourceType": connection_type,
        "permissionObject": {
            "name": _permission_name,
            "objNames": [
                obj_names
            ],
            "objType": obj_type,
            "operations": _operations,
            "permissionType": "highRiskOperation"
        },
        "permissionType": "highRiskOperation"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return _permission_name


def delete_high_risk_source_permission(connection_name, permission_name, _perm_type=7):
    """
    删除高危权限名
    :return:
    """
    _permission_id = db_manage_public.get_permission_id(connection_name, permission_name, _perm_type)
    url = "{}/user/permission".format(base_url)
    payload = "[\n  \"{}\"\n]".format(_permission_id)
    # payload = "[{}]".format(_permission_id.encode("utf-8"))
    headers = {
        'Cookie': public.get_cookie(),
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text


def delete_all_high_risk_source_permission(connection_name, _perm_type=7):
    """
    删除所有高危权限名
    :return:
    """
    _permission_ids = db_manage_public.get_permission_ids(connection_name, _perm_type)
    for i in _permission_ids:
        delete_high_risk_source_permission(connection_name, i, _perm_type)


if __name__ == "__main__":
    # for i in range(0, 5000):
    # operations = ["Delete", "Create_table", "Insert", "Update", "Alter"]
    # operations = ["Insert"]
    # print(add_high_risk_source_permission_oracle(operations, "zyx_test4038_oracle"))
    # print(add_high_risk_source_permission_oracle(operations, "zyx_test4038_oracle", "XYZ_SCHEMA_5519"))
    # print(add_high_risk_source_permission_oracle(operations, "zyx_test4038_oracle", "XYZ_SCHEMA_5519"))
    #
    # print(add_high_risk_source_permission_mysql(operations, "zyx_test4038_mysql", "zyx_schema1267", "表", "zyx_biao7531", "b"))
    # delete_all_high_risk_source_permission("zyx_test4038_oracle")
    # print(delete_permission("zyx_test4265_mysql", "zyx_权限65044"))
    # print(add_high_risk_source_permission_pg(operations, "zyx_test4038_PostgreSQL", "zyx_database1546", "zyx_schema1986", "表", "zyx_biao2519", "A"))
    # print(add_high_risk_source_permission_sqlserver(operations, "zyx_test4038_SqlServer", "zyx_database2454", "zyx_schema6290", "表", "zyx_biao1794", "A"))
    # print(add_high_risk_source_permission_oracle_cdb(operations, "zyx_test1039_oracleCDB"))
    # delete_high_risk_source_permission("zyx_test4038_oracle", "zyx_36274")
    # print(add_high_risk_source_permission_oracle(operations, "zyx_test4038_oracle"))
    # ###################mysql操作#######################
    # print(add_high_risk_source_permission_mysql(operations, "zyx_test4038_mysql", "zyx_schema1267", "表", "zyx_biao7531", "b"))
    # print(add_high_risk_source_permission_mysql(operations, "zyx_test4038_mysql", "zyx_schema1267"))
    # delete_all_high_risk_source_permission("zyx_test4038_mysql")
    # create_table = 'CREATE TABLE `zyx_schema1267`.`table` ( `a` char(22) null)'
    # _insert = 'insert into `zyx_schema1267`.`table` (`a`) values ("2")'
    # _update = 'update `zyx_schema1267`.`table` set `a` = "3" where `a` = "2"'
    # _delete = 'delete from `zyx_schema1267`.`table` where `a` = "3"'
    # delete_all_high_risk_source_permission("xyz_test6666_oracle")
    # _permission_ids = db_manage_public.get_permission_ids("zyx_test6666_oracle",7)
    # print(_permission_ids)
    # delete_all_high_risk_source_permission("xyz_test6666_oracle")
    # delete_high_risk_source_permission("xyz_test6666_oracle", "flowProcessApply")
    print(add_high_risk_source_permission_yes_database(["Insert"], "xyz_test6666_PostgreSQL", "salespdb", "GAOWEI_SCHEMA", "表", "BIAO3333"))
    # "GAOWEI_SCHEMA", "表", "BIAO3333"