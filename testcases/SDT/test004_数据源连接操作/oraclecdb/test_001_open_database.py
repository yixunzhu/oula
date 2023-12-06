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


def test_001_open_database(fixture_delete_all_db_connection):
    """
    打开oraclecdb的database
    :param fixture_delete_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    _db_connection = db_sql.create_db_connection("oraclecdb")
    res = sdt_click.sdt_open_database(_db_connection)
    assert '"resCode":10000,"resMsg":"成功"' in res
    res = json.loads(res)
    nodeName = jsonpath.jsonpath(res, "$.data..nodeName")
    assert len(nodeName) > 0


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
