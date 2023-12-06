# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2021/6/11'


import pytest
import json
import requests
from tins.config import *


url = "url"


def test_001():
    """
    不用传参
    :return:
    """
    payload = ""
    headers = {
        'app-id': 'ypdj',
        'app-version': '1.0',
        'app-platform': 'wxApp',
        'Content-Type': 'text/plain'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert " " in response.text


def test_002(fixture_login):
    """
    需要传参
    :return:
    """

    assert fixture_login()+1 == 2


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
