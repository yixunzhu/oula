# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/4/6'

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


def add_desensitization_resource(connection_name, switch="yes", username="enmoadmin"):
    """
    增加脱敏权限
    :param connection_name: 连接名称
    :return:
    """
    _random = random.randint(10000, 99999)
    _permission_name = "zyx_tm{}".format(_random)
    connection_id = get_connection_id(connection_name)
    _data_type = get_data_type(connection_name)
    url = "{}/user/permission/permission".format(base_url)
    # payload = {
    #     "dataSourceType": _data_type,
    #     "permissionObject": {
    #         "name": _permission_name,
    #         "objNames": [
    #             "/root/0/{}".format(connection_id)
    #         ],
    #         "objType": "connection",
    #         "permissionType": "dataExport",
    #         "exportNum": int(export_num)
    #     },
    #     "permissionType": "dataExport"
    # }
    if _data_type == "Oracle":
        _objNames = "/root/0/{}/TB_SCHEMA/表/TB_TUOMIN/列组/a".format(connection_id)
        _permissionId = "{}/TB_SCHEMA/TB_TABLE/a.dataMaskOpName#column".format(connection_name)
    elif _data_type == "OracleCDB":
        _objNames = "/root/0/{}/SALESPDB/TB_SCHEMA/表/TB_TUOMIN/列组/a".format(connection_id)
        _permissionId = ""
    elif _data_type == "MySQL":
        _objNames = "/root/0/{}/TB_SCHEMA/表/TB_TUOMIN/a".format(connection_id)
        _permissionId = ""
    elif _data_type == "SQLServer":
        _objNames = "/root/0/{}/SALESPDB/TB_SCHEMA/表/TB_TUOMIN/a".format(connection_id)
        _permissionId = ""
    elif _data_type == "PostgreSQL":
        _objNames = "/root/0/{}/salespdb/TB_SCHEMA/表/TB_TUOMIN/a".format(connection_id)
        _permissionId = ""
    else:
        _objNames = ""
        _permissionId = ""
    payload = {
        "dataSourceType": _data_type,
        "permissionObject": {
            "name": _permission_name,
            "description": _permission_name,
            "objNames": [
                _objNames
            ],
            "objType": "column",
            "permissionType": "Desensitization",
            "maskAlgorithm": "MASKING",
            "algorithmParam": {
                "front": 1,
                "count": "7",
                "target": "*"
            },
            "fieldType": "CHAR"
        },
        "permissionType": "Desensitization",
        "permissionId": _permissionId
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if '"resCode":10000' in response.text:
        if switch == "yes":
            switch_desensitization_resource(connection_name, _permission_name)
        return response.text
    else:
        return response.text


def get_list_desensitization_resource(connection_name, username="enmoadmin"):
    """
    获取脱敏资源权限的列表
    :param connection_name:
    :param username:
    :return:
    """
    connection_type = get_data_type(connection_name)
    connection_id = public.get_connection_id(connection_name)
    url = "{}/user/permission/datasource/list".format(base_url)
    payload = {
        "connectionId": connection_id,
        "dataSourceType": connection_type,
        "permType": "Desensitization"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def get_internal_id_desensitization_resource(connection_name, username="enmoadmin"):
    """
    获取脱敏资源权限的internalId列表
    :param connection_name:
    :param username:
    :return:list
    """
    _list_desensitization_resource = get_list_desensitization_resource(connection_name, username)
    res = json.loads(_list_desensitization_resource)
    internalId_list = jsonpath.jsonpath(res, "$..dataSourcePermissionInfos")
    if internalId_list == [[]]:
        return []
    else:
        return jsonpath.jsonpath(res, "$..dataSourcePermissionInfos..internalId")


def get_internal_id_by_desensitization_resource_name(connection_name, resourceName, username="enmoadmin"):
    """
    通过resourceName，脱敏资源名称，获取internal_id
    :param connection_name:
    :param resourceName:
    :param username:
    :return:
    """
    _list_desensitization_resource = get_list_desensitization_resource(connection_name, username)
    res = json.loads(_list_desensitization_resource)
    internalId_list = jsonpath.jsonpath(res, "$..dataSourcePermissionInfos")
    if internalId_list == [[]]:
        return ""
    else:
        internal_id = \
            jsonpath.jsonpath(res,
                              "$..dataSourcePermissionInfos[?(@.resourceName=='{}')].internalId".format(resourceName))[
                0]
        return str(internal_id)


def switch_desensitization_resource(connection_name, resourceName, switch="yes", username="enmoadmin"):
    """
    开关脱敏资源权限，默认开
    :param connection_name:
    :param resourceName:
    :param switch:
    :param username:
    :return:
    """
    url = "{}/user/permission/permission/change/mask/status".format(base_url)
    true = True
    false = False
    if switch == "yes":
        _status = true
    else:
        _status = false
    payload = {
        "internalId": get_internal_id_by_desensitization_resource_name(connection_name, resourceName, username),
        "status": _status
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == '__main__':
    # aa = get_list_desensitization_resource("zyx_test1705_oracle")
    # bb = json.loads(aa)
    # cc = jsonpath.jsonpath(bb, "$..dataSourcePermissionInfos..internalId")
    # print(cc)
    # # print(get_list_desensitization_resource("zyx_test1705_oracle"))
    # a = switch_desensitization_resource("zyx_test1705_oracle", "zyx_test")
    # print(a)
    a = add_desensitization_resource("zyx_test6895_PostgreSQL")
    print(a)
