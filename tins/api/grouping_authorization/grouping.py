# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/3/23'

import json
import time
from tins.api import public
from tins.api.public import *
from tins import config
import requests
import random
# from tins.api.db_connection_info import *
from tins.api import db_connection_info
from tins.config import *
from tins.api.direct_database import drive
import requests


def get_grouping_info(username="enmoadmin"):
    """
    获取分组授权首页信息
    :param username:
    :return:
    """
    url = "{}/user/group/list".format(base_url)
    headers = {
        'Cookie': '{}'.format(get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def get_grouping_id(projectGroupName="", username="enmoadmin"):
    """
    通过分组的名称获取其对应的id
    :param projectGroupName:
    :param username:
    :return:
    """
    _grouping_info = get_grouping_info(username)
    dict_res = json.loads(_grouping_info)
    _id = jsonpath.jsonpath(dict_res, "$.data[?(@.projectGroupName=='{}')].id".format(projectGroupName))[0]
    return str(_id)


def add_grouping(connection_name="", username="enmoadmin"):
    """
    增加分组
    :param connection_name:
    :param username:
    :return:
    """
    _random = random.randint(1000, 99999)
    url = "{}/user/group/add".format(base_url)
    if connection_name != "":
        _connection_name_list = connection_name.split(',')
        _connectionList = []
        for i in _connection_name_list:
            connection_id = get_connection_id(i)
            data_type = get_data_type(i)
            v = {
                "connectionId": connection_id,
                "connectionName": i,
                "connectionType": data_type
            }
            _connectionList.append(v)
        payload = {
            "name": "zyx_grouping分组{}".format(_random),
            "connectionList": _connectionList
        }
    else:
        payload = {
            "name": "zyx_grouping分组{}".format(_random)
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def delete_grouping(projectGroupName="", username="enmoadmin"):
    """
    删除具体的分组名称
    :param projectGroupName:
    :param username:
    :return:
    """
    _id = get_grouping_id(projectGroupName, username)
    url = "{}/user/group/{}".format(base_url, _id)
    headers = {
        'Cookie': '{}'.format(get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers)
    return response.text


def delete_all_grouping(projectGroupName="zyx_grouping", username="enmoadmin"):
    """
    删除所有的分组名称
    :param projectGroupName:
    :param username:
    :return:
    """
    _grouping_info = get_grouping_info(username)
    res = json.loads(_grouping_info)
    _projectGroupName = jsonpath.jsonpath(res, "$.data..projectGroupName")
    for i in _projectGroupName:
        if projectGroupName in i:
            delete_grouping(i, username)
        elif projectGroupName.lower() == "all":
            delete_grouping(i, username)


def run(n=1):
    for i in range(0, n):
        add_grouping()


if __name__ == '__main__':
    # print(add_grouping("lxin_mysql,lxin_orcl"))
    # print(get_prouping_info())
    # print(delete_grouping("nihao"))
    delete_all_grouping()
    # run(500)

