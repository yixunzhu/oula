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


def test_001_right_schema(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    右键schema
    :return:
    """
    fixture_delete_all_db_connection()
    connection_name_list = fixture_create_all_db_connection()
    for i in connection_name_list:
        _data_type = public.get_data_type(i)
        if _data_type == "OracleCDB" or _data_type == "SQLServer" or _data_type == "PostgreSQL":
            res = sdt_click.sdt_database_schema_right_click(i, "SALESPDB", "TB_SCHEMA")
            res = json.loads(res)
            _menu_name_list = jsonpath.jsonpath(res, "$.data..menuName")
            _valid_list = jsonpath.jsonpath(res, "$.data..valid")
            new_menu_name_list = []
            for ii, iii in zip(_valid_list, _menu_name_list):
                if ii:
                    new_menu_name_list.append(iii)
            _data_type = public.get_data_type(i)
            print(_data_type, new_menu_name_list)
            assert set(db_connection_info.db_schema_right_click_info[_data_type]) == set(new_menu_name_list)
        elif _data_type == "Oracle" or _data_type == "MySQL" or _data_type == "DamengDB" or _data_type == "DB2":
            res = sdt_click.sdt_schema_right_click(i, "TB_SCHEMA")
            res = json.loads(res)
            _menu_name_list = jsonpath.jsonpath(res, "$.data..menuName")
            _valid_list = jsonpath.jsonpath(res, "$.data..valid")
            new_menu_name_list = []
            for ii, iii in zip(_valid_list, _menu_name_list):
                if ii:
                    new_menu_name_list.append(iii)
            _data_type = public.get_data_type(i)
            print(_data_type, new_menu_name_list)
            assert set(db_connection_info.db_schema_right_click_info[_data_type]) == set(new_menu_name_list)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
