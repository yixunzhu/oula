# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/11/19'

from tins.api import public
from tins import config
import requests
import jsonpath
import json


# def get_connection_id(link_name):
#     """
#     获取connection_id
#     :return:
#     """
#     url = "{}/dms/meta/node".format(config.base_url)
#     payload = {
#         "nodeType": "root",
#         "nodePath": "/root"
#     }
#     headers = {
#         'Cookie': '{}'.format(public.get_cookie()),
#         'Content-Type': 'application/json'
#     }
#     payload = json.dumps(payload)
#     response = requests.request("POST", url, headers=headers, data=payload)
#     dict_res = json.loads(response.text)
#     connection_id = jsonpath.jsonpath(dict_res, "$.data[?(@.nodeName=='{}')].connectionId".format(link_name))[0]
#     return str(connection_id)


def allow_auto_submit(variable_value=0):
    """
    允许自动提交，默认为开，
    0：开
    1：关
    :return:
    """
    url = "{}/user/connections/conectionSetting".format(config.base_url)
    if str(variable_value) == "0":
        _variable_value = "true"
    else:
        _variable_value = "false"
    payload = {
        "connectionId": 21,
        "variable": "allowAutoCommit",
        "variable_value": "{}".format(_variable_value)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == "__main__":
    # allow_auto_submit(2)
    # print(get_connection_id("zyx_test6646_oracle"))
    pass
