# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/9'

import requests
import json
from tins.api import public
import jsonpath
from tins.api import db_sql
from tins.api.data import _insert, _create, _alter, _create_index, _create_view, _delete, _drop_index, _select, \
    _update

"""
zyx_test7665_oracle
XYZ_SCHEMA_9915
BIAO4997
"""
base_url = "http://192.168.3.144"

_sql_list = [_insert, _insert, _create, _alter, _create_index, _create_view, _delete, _drop_index, _select, _update]
_sql_list1 = []
sql_list2 = []
sql_list3 = []
sql_list4 = []
sql_list5 = []
sql_list6 = []
sql_list7 = []
sql_list8 = []
sql_list9 = []
sql_list10 = []
_authority_list = [
    "Alter",
    "Drop",
    "Delete",
    "Insert",
    "Select",
    "Update",
    "Execute",
    "Truncate",
    "Terminal",
    "Merge",
    "OtherDDL",
    "aabb"
]


def get_id_list(username="enmoadmin"):
    url = "{}/user/oracleAudit/findOperateTypes".format(base_url)
    headers = {
        'Cookie': public.get_cookie(username)
    }
    response = requests.request("GET", url, headers=headers)
    res = json.loads(response.text)
    id = jsonpath.jsonpath(res, "$.data..id")
    return id


def add_operate_type(content=["Insert"], operate_type=1, username="enmoadmin"):
    """
    添加高危
    :param content:
    :param operate_type:
    :param username:
    :return:
    """
    for i in content:
        _operate_type = str(operate_type)
        # if str(operate_type) == "1":
        #     _operate_type = str(operate_type)
        # else:
        #     _operate_type = str(operate_type)
        url = "{}/user/oracleAudit/insertOperateType".format(base_url)
        payload = {
            "content": i,
            "operateType": _operate_type
        }
        payload = json.dumps(payload)
        headers = {
            'Cookie': public.get_cookie(username),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)


def delete_all(username="enmoadmin"):
    id_list = get_id_list()
    print(id_list)
    for i in id_list:
        print(i)
        url = "{}/user/oracleAudit/deleteOperateType?id={}".format(base_url, i)
        headers = {
            'Cookie': public.get_cookie(username),
            'Content-Type': 'text/plain'
        }
        response = requests.request("DELETE", url, headers=headers)
        print(response.text)


def run_sql(sql="", schema_name="XYZ_SCHEMA_9915", connection_name="zyx_test7665_oracle"):
    res = db_sql.run_sql_oracle(connection_name, sql, schema_name)
    return res


def run():
    _sql_list = [_insert, _insert, _create, _alter, _create_index, _create_view, _delete, _drop_index, _select, _update]
    _sql_list1 = [_insert]
    sql_list2 = []
    sql_list3 = []
    sql_list4 = []
    sql_list5 = []
    sql_list6 = []
    sql_list7 = []
    sql_list8 = []
    sql_list9 = []
    sql_list10 = []
    for i in _sql_list:
        # print(run_sql('SELECT * FROM "XYZ_SCHEMA_9915"."BIAO4997"'))
        print(run_sql(i))


if __name__ == "__main__":
    # delete_all()
    add_operate_type(_authority_list, 3)
    # add_operate_type(["Insert"], 3)
    # run()
