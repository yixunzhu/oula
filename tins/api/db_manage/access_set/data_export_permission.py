# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/12/3'

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


# def get_permission_info(connection_name):
#     """
#     获取权限页面的信息
#     :param connection_name:
#     :return:
#     """
#     connection_id = get_connection_id(connection_name)
#     _data_type = get_data_type(connection_name)
#     url = "{}/user/permission/datasource/list".format(base_url)
#     payload = {
#         "connectionId": connection_id,
#         "dataSourceType": _data_type,
#         "permType": "dataSource"
#     }
#     payload = json.dumps(payload)
#     headers = {
#         'Cookie': '{}'.format(public.get_cookie()),
#         'Content-Type': 'application/json'
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
#     res = json.loads(response.text)
#     return res
#
#
# def get_permission_id(connection_name, permission_name):
#     res = get_permission_info(connection_name)
#     permission_id = jsonpath.jsonpath(res,
#                                       "$..dataSourcePermissionInfos[?(@.permissionName=='{}')].permissionId".format(
#                                           permission_name))[0]
#     return str(permission_id)
#
#
# def get_permission_ids(connection_name):
#     """
#     获取所有的permission_ids
#     :param connection_name:
#     :return: list[]
#     """
#     res = get_permission_info(connection_name)
#     # permission_id = jsonpath.jsonpath(res,
#     #                                   "$..dataSourcePermissionInfos[?(@.permissionName)].permissionId"[0])
#     permission_id = jsonpath.jsonpath(res, "$..permissionName")
#     for i in permission_id:
#         if "zyx_权限" not in i:
#             permission_id.remove(i)
#     return permission_id

def get_data_export_permission_name(connection_name):
    """
    获取"数据库"为"全部"的权限名称
    :param connection_name:
    :return:
    """
    _info = db_manage_public.get_permission_info(connection_name, 2)
    permission_name = jsonpath.jsonpath(_info, "$.data.dataSourcePermissionInfos[?(@.database=='{}')].permissionName".format("全部"))[0]
    return permission_name


def add_data_export_permission(connection_name, export_num=-1):
    """
    增加数据操作权限，默认添加数据连接的
    :param connection_name: 连接名称
    :return:
    """
    _random = random.randint(10000, 99999)
    _permission_name = "zyx_权限{}".format(_random)
    connection_id = get_connection_id(connection_name)
    _data_type = get_data_type(connection_name)
    url = "{}/user/permission/permission".format(base_url)
    payload = {
        "dataSourceType": _data_type,
        "permissionObject": {
            "name": _permission_name,
            "objNames": [
                "/root/0/{}".format(connection_id)
            ],
            "objType": "connection",
            "permissionType": "dataExport",
            "exportNum": int(export_num)
        },
        "permissionType": "dataExport"
    }
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    if "权限已存在" in response.text:
        _permission_name_ = get_data_export_permission_name(connection_name)
        # return _permission_name_
        delete_data_export_permission(connection_name, _permission_name_)
        response = requests.request("POST", url, headers=headers, data=payload)
        return _permission_name
    else:
        return _permission_name


def delete_data_export_permission(connection_name, permission_name):
    """
    删除的权限名
    :return:
    """
    _permission_id = db_manage_public.get_permission_id(connection_name, permission_name, 2)
    url = "{}/user/permission".format(base_url)
    payload = "[\n  \"{}\"\n]".format(_permission_id)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    # print(response.text)


def delete_all_data_export_permission(connection_name):
    """
    删除所有权限名
    :return:
    """
    _permission_ids = db_manage_public.get_permission_ids(connection_name, 2)
    for i in _permission_ids:
        delete_data_export_permission(connection_name, i)


if __name__ == "__main__":
    # aa()
    print(delete_all_data_export_permission("zyx_test6646_oracle"))
    # print(delete_data_export_permission("zyx_test6646_oracle", "zyx_权限34995"))
    # delete_all_permission("zyx_test4265_mysql")
