# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.db_sql import *
from tins.api import public
from tins.api.db_manage.access_set import role_manage
from tins.api.flow import apply_flow
from tins.api import notice
from tins.data_factory.sql_data import *


def test_001_data_correction_flow(fixture_create_all_db_connection, fixture_delete_all_db_connection):
    """
    数据订正提权
    步骤：
    1、管理员新建数据源连接,此时断言新用户A申请数据订正提权，界面中无数据源连接
    2、普通用户进行提权订正流程，管理通过后，此用户进行订正，回退操作
    :param fixture_create_all_db_connection:
    :return:
    """
    fixture_delete_all_db_connection()
    db_connection_list = fixture_create_all_db_connection()
    username = public.create_username_and_update_pw()
    # 新用户A申请数据订正提权，界面中无数据源连接
    _ui_info = apply_flow.get_flow_ui_info(1, username)
    assert '"data":[]' in _ui_info
    for i in db_connection_list:
        role_manage.initialize_role_binding_user(i, username)
        # if "oracle" in i and "oracleCDB" not in i:
        _info = apply_flow.data_correction_flow(i, oracle["insert"], oracle["insert"], username)
        _info = json.loads(_info)
        _id = _info["data"]
        # 管理员/审批进行审批通过
        notice.flow_audit(_id, "yes")
        _v1 = notice.view_notice(_id, username)
        # 订正
        _v2 = notice.execute(_id, username)
        # 回退
        _v3 = notice.rollback(_id, username)
        assert '"resCode":10000,"resMsg":"成功"' in _v1
        assert '"resCode":10000,"resMsg":"成功"' in _v2
        assert '"resCode":10000,"resMsg":"成功"' in _v2

    public.delete_username(username)


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
