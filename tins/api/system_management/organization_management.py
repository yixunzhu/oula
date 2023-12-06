# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/30'


import jsonpath
import requests
import json
from tins.config import *
import random
from tins.api import public
from tins.api.public import *


def get_organization_info(username="enmoadmin"):
    """
    获取用户列表
    :param username:
    :return:
    """
    url = "{}/user/users/dept/cqUser".format(base_url)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


if __name__ == '__main__':
    print(get_organization_info())
