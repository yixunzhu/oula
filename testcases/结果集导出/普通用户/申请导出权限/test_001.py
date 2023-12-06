# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'


import pytest
import json
import requests
from tins.config import *


def test_001():
    """
    不用传参
    :return:
    """
    pass


def test_002(fixture_create_db_connection_and_schema_and_table_and_insert_oracle):
    """
    需要传参
    :return:
    """

    pass


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
