# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
from tins.api import db_sql
from tins.api import db_connection_info
from tins.api.public import *


def test_001_open_schema(fixture_delete_all_db_connection):
    """
    打开oraclecdb的schema
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("oraclecdb")
    connection_type = get_data_type(_db_connection)
    res = sdt_click.sdt_open_schema(_db_connection)
    res = json.loads(res)
    nodeName = jsonpath.jsonpath(res, "$.data..nodeName")
    assert set(nodeName) == set(db_connection_info.db_open_schema_info[connection_type])


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
