# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/12/3'

import json
import time
from tins.api import public
from tins.api.public import *
from tins import config
import requests
import random
from tins.api import db_connection_info
from tins.config import *
from tins.api.db_manage import db_manage_public


def high_risk_review_settings(connection_name, variable_value=0, username="enmoadmin"):
    """
    连接管理-通用配置-高危复核设置的设置，默认"NONE",0
    :param connection_name:
    :param variable_value:
    :param username:
    :return:
    """
    _variable_value = "NONE" if variable_value == 0 else "OTP"
    url = "{}/user/connections/conectionSetting".format(base_url)
    payload = {
        "connectionId": public.get_connection_id(connection_name),
        "variable": "highRiskCheck",
        "variable_value": _variable_value
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': public.get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == '__main__':
    print(high_risk_review_settings("zyx_test4038_oracle",1))
