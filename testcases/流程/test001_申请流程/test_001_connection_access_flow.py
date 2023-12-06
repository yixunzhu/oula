# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
import random
from tins.api import public
from tins.api.db_manage.access_set import role_manage
from tins.api.flow import apply_flow
from tins.api import notice
from tins.api import db_sql


def test_001_connection_access_flow(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    连接访问提权
    步骤：
    1、管理员新建数据源连接
    2、普通用户进行申请访问提权
    3、对应审核员审核通过
    断言：
    普通员工可以访问
    校验：
    1、管理员新建数据源连接
    2、普通用户进行申请访问提权
    3、对应审核员审核拒绝通过
    断言：
    普通员工不可以访问
    :param fixture_create_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    new_user = public.create_username_and_update_pw()
    for i in db_connection_list:
        _info = apply_flow.connection_access_flow(i, new_user)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员先进行审批拒绝
        notice.flow_audit(_id, "no")
        __info = public.get_info(new_user)
        assert i not in str(__info)
        # 普通用户再次提权
        _info = apply_flow.connection_access_flow(i, new_user)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批员在进行审批通过
        notice.flow_audit(_id)
        __info = public.get_info(new_user)
        assert i in str(__info)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
