# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
from tins.api import db_sql
from tins.api import public
from tins.api import db_connection_info
from tins import config
import requests


def test_001_create_table(fixture_delete_all_db_connection):
    """
    添加表
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("pg")
    res = sdt_click.sdt_right_click_create_table(_db_connection)
    assert '"resCode":10000,"resMsg":"成功"' in res


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
