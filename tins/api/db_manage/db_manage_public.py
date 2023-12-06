# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/12/7'

import json
import jsonpath
from tins.api import public
from tins.api.public import *
from tins import config
import requests


def get_permission_info(connection_name, _perm_type=1):
    """
    获取权限页面的信息
    :param connection_name:
    :perm_type 权限的类型如下：
    1：代表数据源操作权限
    2：数据导出权限
    3：过滤权限
    4：执行次数权限
    5：执行行数权限
    6：执行时间权限
    7：高危资源
    8：脱敏资源
    默认为1，即：数据源操作权限
    :return:
    """
    connection_id = get_connection_id(connection_name)
    _data_type = get_data_type(connection_name)
    if int(_perm_type) == 1:
        perm_type = "dataSource"
    elif int(_perm_type) == 2:
        perm_type = "dataExport"
    elif int(_perm_type) == 3:
        perm_type = "objectFilter"
    elif int(_perm_type) == 4:
        perm_type = "executeTimes"
    elif int(_perm_type) == 5:
        perm_type = "executeRows"
    elif int(_perm_type) == 6:
        perm_type = "executeDate"
    elif int(_perm_type) == 7:
        perm_type = "highRiskOperation"
    elif int(_perm_type) == 8:
        perm_type = "Desensitization"

    url = "{}/user/permission/datasource/list".format(base_url)
    payload = {
        "connectionId": connection_id,
        "dataSourceType": _data_type,
        "permType": perm_type
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    return res


def get_permission_id(connection_name, permission_name, _perm_type=1):
    """
    获取单个权限名的permission_id
    :param connection_name:
    :param permission_name:
    :perm_type 权限的类型如下：
    1：代表数据源操作权限
    2：数据导出权限
    3：过滤权限
    4：执行次数权限
    5：执行行数权限
    6：执行时间权限
    7：高危资源
    8：脱敏资源
    默认为1，即：数据源操作权限
    :return:
    """
    res = get_permission_info(connection_name, _perm_type)
    permission_id = jsonpath.jsonpath(res,
                                      "$..dataSourcePermissionInfos[?(@.permissionName=='{}')].permissionId".format(
                                          permission_name))[0]
    return str(permission_id)


def get_permission_ids(connection_name, _perm_type=1):
    """
    获取所有的permission_ids
    :param connection_name:
    :perm_type 权限的类型如下：
    1：代表数据源操作权限
    2：数据导出权限
    3：过滤权限
    4：执行次数权限
    5：执行行数权限
    6：执行时间权限
    7：高危资源
    8：脱敏资源
    默认为1，即：数据源操作权限
    :return: list[]
    """
    res = get_permission_info(connection_name, _perm_type)
    infos = jsonpath.jsonpath(res, "$..dataSourcePermissionInfos")
    if infos == [[]]:
        permission_id = []
        return permission_id
    else:
        permission_id = jsonpath.jsonpath(res, "$..permissionName")
        for i in permission_id:
            if "zyx_" not in i and "flowProcessApply" != i:
                permission_id.remove(i)
        return permission_id


if __name__ == "__main__":
    # print(get_permission_id("zyx_test8097_oracle", "zyx_权限74001", 7))
    print(get_permission_ids("xyz_test6666_oracle", 7))
    # print(get_permission_info("xyz_test6666_oracle", 7))
