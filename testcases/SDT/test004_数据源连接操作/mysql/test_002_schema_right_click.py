# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.public import *
import json
from tins.api import db_sql
from tins.api import public
from tins import config
import requests


def test_001_create_schema(fixture_delete_all_db_connection):
    """
    添加数据库
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("mysql")
    connection_type = get_data_type(_db_connection)
    url = "{}/dms/statement/execute".format(config.base_url)
    connection_id = public.get_connection_id(_db_connection)
    payload = {
        "connectionId": connection_id,
        "dataSourceType": connection_type,
        "statements": [
            " CREATE DATABASE IF NOT EXISTS `TB_SCHEMA`\n "
        ],
        "tabKey": "ALL",
        "actionType": "EXECUTE"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert '"resCode":10000,"resMsg":"成功"' in response.text


def test_002_export(fixture_delete_all_db_connection):
    """
    右键导出
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("mysql")
    connection_type = get_data_type(_db_connection)
    url = "{}/export/export/menu".format(config.base_url)
    connection_id = public.get_connection_id(_db_connection)
    payload = {
        "dumpType": "DUMPSTRUCTURE",
        "fileName": "10000000",
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeName": "TB_SCHEMA",
        "nodeType": "oracleUser",
        "nodePath": "/root/{}/TB_SCHEMA".format(connection_id)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert '{"resCode":10000,"resMsg":"成功","data":true}' in response.text


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
