# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/12/3'

from tins.api.connection_management import general_configuration
from tins.api.public import *
from tins.config import *


def initialize_role_binding_user(connection_name, user):
    """
    初始化角色绑定用户
    connection_name:连接名称
    user：用户
    :return:
    """
    url = "{}/user/connection/grant/user".format(base_url)
    connection_id = get_connection_id(connection_name)
    if type(user) == str:
        grant_user = ["{}".format(user)]
    elif type(user) == list:
        grant_user = user
    payload = {
        "grantUser": grant_user,
        "roleName": "{}_初始化角色_{}".format(connection_name, connection_id),
        "connectionId": connection_id
    }
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def add_role(connection_name="", user=""):
    """
    添加角色
    :param connection_name:
    :param user:
    :return:
    """
    connection_id = general_configuration.get_connection_id(connection_name)
    _random = random.randint(10000, 99999)
    _role_name = "zyx_角色{}".format(_random)
    url = "{}/user/connection".format(base_url)
    if user != "":
        if type(user) == str and user != "":
            grant_user = ["{}".format(user)]
        elif type(user) == list:
            grant_user = user
        payload = {
            "type": "DATASOURCE",
            "name": _role_name,
            "connectionId": connection_id,
            "grantUser": grant_user
        }
    else:
        payload = {
            "type": "DATASOURCE",
            "name": _role_name,
            "connectionId": connection_id,
        }
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    print(payload)
    requests.request("POST", url, headers=headers, data=payload)
    return _role_name


def authorization():
    """
    授权
    :return:
    """
    pass


if __name__ == "__main__":
    print(add_role("zyx_test6646_oracle"))
