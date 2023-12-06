# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/2/25'

import requests
from tins.config import *


def get_version_info():
    """
    获取版本信息
    :return: str
    """
    url = "{}/user/versionInfo".format(base_url)
    response = requests.request("GET", url)
    return response.text


