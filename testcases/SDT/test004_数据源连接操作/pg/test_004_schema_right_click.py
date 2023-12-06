# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
from tins.api import db_sql
from tins.api import public
from tins.api.public import *
from tins import config
import requests


def test_001_schema_right_click(fixture_delete_all_db_connection):
    """
    schema右键点击
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("pg")
    connection_type = get_data_type(_db_connection)
    url = "{}/dms/meta/menus".format(config.base_url)
    connection_id = public.get_connection_id(_db_connection)
    payload = {
        "connectionId": connection_id,
        "connectionType": connection_type,
        "nodeType": "schema",
        "nodeName": "TB_SCHEMA",
        "nodePath": "/root/{}/{}/{}".format(connection_id, "salespdb", "TB_SCHEMA"),
        "nodePermissionLimits": [],
        "userId": "enmoadmin"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert '"resCode":10000,"resMsg":"成功"' in response.text
    assert '添加模式' in response.text


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
