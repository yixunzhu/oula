# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/11/24'

"""
pytest插件

扩展以下pytest参数：
-P参数：testcase优先级过滤
"""

import pytest
# from tins import api
from tins.api import public
from tins.api import db_sql
# from tins.api import connection_management
# from tins.api import db_connection_info
from tins.api.sdt import sdt_click


def pytest_addoption(parser):
    """扩展pytest接收参数的hook
    """
    has_p = False
    for options in parser._anonymous.options:
        if "-P" in options._short_opts:
            has_p = True
    if not has_p:
        parser.addoption("-P", type=int, metavar="NAME",
                         help="only run tests equal or lower than the priority")

    group = parser.getgroup("email reporting")
    group.addoption("--emailresult", "--email-result", action="store", dest="email_result",
                    type=bool, metavar="NAME", default=False,
                    help="set True to send email result.")
    group.addoption("--emailformat", "--email-format", action="store", dest="email_format",
                    type=int, metavar="NAME",
                    help="Email format. 0-No Email; 1-Daily Email Format; 2-Manual Email Format.")
    group.addoption("--retrytime", "--retry-time", action="store", dest="retry_time", type=int,
                    metavar="NAME", help="Failed case retry times to re-run.")
    group.addoption("--emaillist", "--email-list", action="store", dest="email_list", type=int,
                    metavar="NAME", help="Add new email list.")


@pytest.fixture(scope="module")
def fixture_login():
    """
    登录测试固件方法
    :param request:
    :return:
    """
    def _fixture_login(user_id="enmoadmin", password="Hello123$"):
        return public.login(user_id, password)

    return _fixture_login


@pytest.fixture(scope="module")
def fixture_create_db_connection():
    def _fixture_create_db_connection(type_connection="oracle"):
        return db_sql.create_db_connection(type_connection)
    return _fixture_create_db_connection


@pytest.fixture(scope="module")
def fixture_create_all_db_connection():
    """
    新建所有类型的数据源连接
    :return:
    """
    def _fixture_create_all_db_connection(private_connection=0, dev_model=0):
        connection_name_list = db_sql.create_all_db_connection(private_connection, dev_model)
        return connection_name_list
        # return db_sql.create_all_db_connection()
        # db_list = list(db_connection_info.db_connections.keys())
        # connection_name_list = []
        # for i in db_list:
        #     connection_name = db_sql.create_db_connection(i)
        #     if "失败" not in connection_name:
        #         connection_name_list.append(connection_name)
        # return connection_name_list
    return _fixture_create_all_db_connection


@pytest.fixture(scope="module")
def fixture_delete_db_connection():
    """
    删除数据源连接
    :return:
    """
    def _fixture_delete_db_connection(_db_connection_name):
        db_sql.delete_db_connection_name(_db_connection_name)
    return _fixture_delete_db_connection


@pytest.fixture(scope="module")
def fixture_delete_all_db_connection():
    """
    删除所有数据源连接
    :return:
    """
    def _fixture_delete_all_db_connection():
        db_sql.delete_all_db_connection_name()
    return _fixture_delete_all_db_connection


@pytest.fixture(scope="module")
def fixture_delete_all_folders():
    """
    删除所有文件夹
    :return:
    """
    def _fixture_delete_all_folders():
        sdt_click.delete_all_folders()
    return _fixture_delete_all_folders


# @pytest.fixture(scope="module")
# def fixture_delete_all_db_connection_schema():
#     """
#     删除所有数据源的schame
#     :return:
#     """
#     def _fixture_delete_all_db_connection_schema():
#         # 先创建数据源连接
#         db_list = list(db_connection_info.db_connections.keys())
#         # connection_name_list = []
#         for i in db_list:
#             if i == "Oracle":
#                 connection_name = db_sql.create_db_connection(i)
#                 db_sql.delete_all_schema_oracle(connection_name)
#             # elif i == "Mysql":
#             #     connection_name = db_sql.create_db_connection(i)
#             #     db_sql.delete_all_schema_oracle(connection_name)
#             # connection_name_list.append(connection_name)
#         db_sql.delete_all_db_connection_name()
#     return _fixture_delete_all_db_connection_schema
#
#
# @pytest.fixture(scope="module")
# def fixture_create_db_connection_and_schema_and_table_and_insert_oracle():
#     def _fixture_create_db_connection_and_schema_and_table_and_insert_oracle(type_connection="mysql", n=10):
#         return db_sql.create_db_connection_and_schema_and_table_and_insert_oracle(type_connection, n)
#
#     return _fixture_create_db_connection_and_schema_and_table_and_insert_oracle
#
#
# @pytest.fixture(scope="module")
# def fixture_reset_environment():
#     def _fixture_reset_environment():
#         sdt_click.delete_all_folders()
#
#         db_list = list(db_connection_info.db_connections.keys())
#         for i in db_list:
#             if i == "Oracle":
#                 connection_name = db_sql.create_db_connection(i)
#                 db_sql.delete_all_schema_oracle(connection_name)
#             # elif i == "Mysql":
#             #     connection_name = db_sql.create_db_connection(i)
#             #     db_sql.delete_all_schema_oracle(connection_name)
#             # connection_name_list.append(connection_name)
#         db_sql.delete_all_db_connection_name()
#     return _fixture_reset_environment