# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/11/19'

import json
import time
from tins.api import public
from tins.api.public import *
from tins import config
import requests
import random
# from tins.api.db_connection_info import *
from tins.api import db_connection_info
from tins.config import *
from tins.api.direct_database import drive
import threading

tabkey = time.time()


def get_id():
    return str(tabkey)


def create_db_connection(type_connection="Oracle", private_connection=0, dev_model=0, username="enmoadmin"):
    """
    创建数据库连接
    :return:
    """
    _private_connection = False if private_connection == 0 else True
    _dev_model = False if dev_model == 0 else True
    url = "{}/dms/connection/configuration".format(base_url)
    false = False
    headers = {
        'Cookie': '{}'.format(get_cookie(username)),
        'Content-Type': 'application/json'
    }
    if db_connection_info.is_db_connection(type_connection.lower()):
        if type_connection.lower() == "oracle":
            payload = db_connection_info.db_connections["Oracle"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["Oracle"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "oraclecdb":
            payload = db_connection_info.db_connections["OracleCDB"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["OracleCDB"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "mysql":
            payload = db_connection_info.db_connections["MySQL"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["MySQL"]["userInputs"]["connectionName"]
            else:
                return "创建{}失败".format("MySQL")
        elif type_connection.lower() in "damengdb" or type_connection.lower() in "dameng":
            payload = db_connection_info.db_connections["DamengDB"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["DamengDB"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "sqlserver":
            payload = db_connection_info.db_connections["SQLServer"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["SQLServer"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "postgresql" or type_connection.lower() in "pg":
            payload = db_connection_info.db_connections["PostgreSQL"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["PostgreSQL"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "mongodb":
            payload = db_connection_info.db_connections["MongoDB"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["MongoDB"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "mogdb":
            payload = db_connection_info.db_connections["MogDB"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["MogDB"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "db2":
            payload = db_connection_info.db_connections["DB2"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["DB2"]["userInputs"]["connectionName"]
        elif type_connection.lower() in "starrocks":
            payload = db_connection_info.db_connections["StarRocks"]
            payload["userInputs"]["privateConnection"] = _private_connection
            payload["userInputs"]["devModel"] = _dev_model
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            if "成功" in response.text:
                return db_connection_info.db_connections["StarRocks"]["userInputs"]["connectionName"]
    else:
        return "{}数据库连接失败".format(type_connection.lower())


def delete_db_connection_name(_db_connection_name):
    """
    删除数据源连接
    :return:
    """
    url = "{}/dms/menu".format(config.base_url)
    payload = {
        "connectionId": get_connection_id(_db_connection_name),
        "nodePath": "/root/0/{}".format(get_connection_id(_db_connection_name)),
        "nodeType": "connection"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text


def delete_all_db_connection_name(_connection_name="all", _connection_name2="zyx_test"):
    """
    删除所有名称为"zyx_test_"的数据源连接
    :return:
    """
    all_db_connection_name = public.get_all_db_connection_name()
    for i in all_db_connection_name:
        if _connection_name2 in i and _connection_name in i:
            delete_db_connection_name(i)
        elif _connection_name2 in i and _connection_name == "all":
            delete_db_connection_name(i)


def create_all_db_connection(private_connection=0, dev_model=0, username="enmoadmin"):
    """
    新建所有类型的数据源连接
    备注：当数据源连接失败时，不创建
    :return:
    """
    _private_connection = False if private_connection == 0 else True
    _dev_model = False if dev_model == 0 else True
    db_list = list(db_connection_info.db_connections.keys())
    connection_name_list = []
    for i in db_list:
        connection_name = create_db_connection(i, _private_connection, _dev_model, username)
        if "失败" not in connection_name:
            connection_name_list.append(connection_name)
    return connection_name_list


# ################################oracleCDB操作################################
def run_sql_oracleCDB(connection_name="", sql="", username="enmoadmin", databaseName="SALESPDB",
                      schema_name="TB_SCHEMA", _auto_commit=0):
    """
    执行oracleCDB的SQL语句
    :return:
    """
    true = True
    false = False
    if int(_auto_commit) == 0:
        auto_commit = true
    else:
        auto_commit = false
    url = "{}/dms/statement/execute".format(config.base_url)
    if type(sql) == str:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "OracleCDB",
            "statements": [
                "{}".format(sql).replace(";", "")
            ],
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(databaseName),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    elif type(sql) == list:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "OracleCDB",
            "statements": sql,
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(databaseName),
            "tabKey": "{}".format(get_id()),
            "autoCommit": auto_commit
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


# ################################oracle操作################################
def get_all_schema_oracle(connection_name):
    """
    获取所有schema的名称
    :param connection_name:
    :return:
    """
    url = "{}/dms/meta/node".format(base_url)
    connection_id = public.get_connection_id(connection_name)
    payload = {
        "connectionId": connection_id,
        "connectionType": "Oracle",
        "nodeType": "connection",
        "nodePath": "/root/{}".format(connection_id)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)["data"]
    _node_name_list = [i["nodeName"] for i in res]
    return _node_name_list[:-1]


def sql_create_schema_oracle():
    """
    创建oracle schema的sql语句，
    :return: list
    """
    _random = random.randint(1000, 9999)
    sql_oracle_schema_list = ['ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE',
                              'CREATE USER XYZ_SCHEMA_{} IDENTIFIED BY 123456'.format(_random),
                              'GRANT CONNECT,RESOURCE TO XYZ_SCHEMA_{}'.format(_random),
                              'alter user XYZ_SCHEMA_{} quota unlimited on users'.format(_random)]
    return sql_oracle_schema_list, "XYZ_SCHEMA_{}".format(_random)


def sql_create_table_oracle(_schema):
    """
    创建oracle table的sql语句，
    :return:
    """
    _random = random.randint(1000, 9999)
    sql2 = """COMMENT ON COLUMN "BIAO{}"."a" IS '哈哈1'""".format(_random)
    sql3 = """COMMENT ON COLUMN "BIAO{}"."b" IS '哈哈2'""".format(_random)
    sql4 = """COMMENT ON COLUMN "BIAO{}"."c" IS '哈哈1'""".format(_random)
    sql1 = """CREATE TABLE
                "{}"."BIAO{}" (
                "a" CHAR(33),
                "b" DATE,
                "c" FLOAT(33),
                "d" FLOAT(33),
                "e" VARCHAR2(33)
              )
            """.format(_schema, _random)
    sql_oracle_table_list = [sql1, sql2, sql3, sql4]
    return sql_oracle_table_list, "BIAO{}".format(_random)


def sql_create_schema_and_create_table_oracle():
    """
    创建schema且创建表的sql语句
    :return:
    """
    a, b = sql_create_schema_oracle()
    _a, _b = sql_create_table_oracle(b)
    return a + _a


def sql_create_schema_and_create_table_and_insert_oracle(n=1):
    a, b = sql_create_schema_oracle()
    _a, _b = sql_create_table_oracle(b)
    _insert = ["""insert into "{}"."{}" ("a","b","c","d","e") values ('111',DEFAULT,111.22,222.111,'aaaaa')
    """.format(b, _b)] * int(n)
    # print(a + _a + _insert)
    return a + _a + _insert


# def delete_schema_oracle(connection_name="", schema_name="", username="enmoadmin", _auto_commit=0):
#     """
#     删除schema
#     :return:
#     """
#     _sql = "DROP USER {} CASCADE".format(schema_name)
#     run_sql_oracle(connection_name, _sql, "", username, _auto_commit)
def delete_schema_oracle(schema_name=""):
    """
    删除schema
    :return:
    """
    drive.delete_schema_oracle(schema_name)


def delete_all_schema_oracle(connection_name, schema_name="XYZ"):
    """
    删除所有XYZ的schema
    :return:
    """
    _get_all_schema_oracle = get_all_schema_oracle(connection_name)
    _get_all_schema = []
    for i in _get_all_schema_oracle:
        if schema_name in i:
            _get_all_schema.append(i)
    drive.delete_all_schema_oracle(_get_all_schema)
    #         # _sql = "DROP USER {} CASCADE".format(i)
    #         # run_sql_oracle(connection_name, _sql)
    #         drive.delete_schema_oracle(i)


def delete_table_oracle(connection_name="", schema_name="", table_name="", username="enmoadmin", _auto_commit=0):
    """
    删除表
    :return:
    """
    _sql = "DROP TABLE {}".format(table_name)
    run_sql_oracle(connection_name, _sql, schema_name, username, _auto_commit)


def run_sql_oracle(connection_name="", sql="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    执行oracle的SQL语句
    :return:
    """
    true = True
    false = False
    if int(_auto_commit) == 0:
        auto_commit = true
    else:
        auto_commit = false
    url = "{}/dms/statement/execute".format(config.base_url)
    if type(sql) == str:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "Oracle",
            "statements": [
                "{}".format(sql).replace(";", "")
            ],
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(schema_name),
            "tabKey": "{}".format(get_id()),
            "autoCommit": auto_commit
        }
    elif type(sql) == list:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "Oracle",
            "statements": sql,
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(schema_name),
            "tabKey": "{}".format(get_id()),
            "autoCommit": auto_commit
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def create_schema_oracle(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    创建oracle schema
    :return:
    """
    # sql = """
    # -- 建库
    # -- CREATE USER
    # ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;
    # CREATE USER XYZ11 IDENTIFIED BY 123456;
    # GRANT CONNECT,RESOURCE TO XYZ11;
    # alter user XYZ11 quota unlimited on users;-- 为用户“XYZ”在users表空间上设置配额（分配无限制的空间）
    # """
    sql, schema_name = sql_create_schema_oracle()
    run_sql_oracle(connection_name, sql, "", username, _auto_commit)
    return schema_name


def create_table_oracle(connection_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    创建表
    :return:
    """
    sql, table_name = sql_create_table_oracle(schema_name)
    run_sql_oracle(connection_name, sql, "", username, _auto_commit)
    return table_name


def create_schema_and_create_table_oracle(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    先创建schema在创建表
    :return:
    """
    schema_name = create_schema_oracle(connection_name, username, _auto_commit)
    table_name = create_table_oracle(connection_name, schema_name, username, _auto_commit)
    return schema_name, table_name


def create_schema_and_create_table_and_insert_oracle(connection_name="", n=1, username="enmoadmin", _auto_commit=0):
    """
    先创建schema在创建表,在插入数据
    :return:
    """
    schema_name, table_name = create_schema_and_create_table_oracle(connection_name, username, _auto_commit)
    _sql_insert = ["""insert into "{}"."{}" ("a","b","c","d","e") values ('111',DEFAULT,111.22,222.111,'aaaaa')
        """.format(schema_name, table_name)] * int(n)
    run_sql_oracle(connection_name, _sql_insert, schema_name, username, _auto_commit)
    return schema_name, table_name, n


def create_db_connection_and_schema_and_table_and_insert_oracle(type_connection="Oracle", n=1, username="enmoadmin",
                                                                _auto_commit=0):
    """
    先后创建连接，schema，表，在插入数据
    :return:
    """
    connection_name = create_db_connection(type_connection, username)
    schema_name, table_name = create_schema_and_create_table_oracle(connection_name, username, _auto_commit)
    _sql_insert = ["""insert into "{}"."{}" ("a","b","c","d","e") values ('111',DEFAULT,111.22,222.111,'aaaaa')
        """.format(schema_name, table_name)] * int(n)
    run_sql_oracle(connection_name, _sql_insert, schema_name, username, _auto_commit)
    return connection_name, schema_name, table_name, n


# mysql操作
def get_all_schema_mysql(connection_name):
    """
    获取所有schema的名称
    :param connection_name:
    :return:
    """
    url = "{}/dms/meta/node".format(base_url)
    connection_id = public.get_connection_id(connection_name)
    payload = {
        "connectionId": connection_id,
        "connectionType": "MySQL",
        "nodeType": "connection",
        "nodePath": "/root/{}".format(connection_id)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)["data"]
    _node_name_list = [i["nodeName"] for i in res]
    return _node_name_list[:-1]


def run_sql_mysql(connection_name="", sql="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    执行mysql的SQL语句
    :return:
    """
    true = True
    false = False
    if int(_auto_commit) == 0:
        auto_commit = true
    else:
        auto_commit = false
    url = "{}/dms/statement/execute".format(config.base_url)
    if type(sql) == str:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "statements": [
                "{}".format(sql).replace(";", "")
            ],
            "segmentIndex": 0,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "MySQL",
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(schema_name),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    elif type(sql) == list:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "statements": sql,
            "segmentIndex": 0,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "MySQL",
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(schema_name),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def create_schema_mysql(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    创建mysql schema
    :return:
    """
    _random = random.randint(1000, 9999)
    sql_create_schema = """CREATE DATABASE IF NOT EXISTS `zyx_schema{}` CHARACTER SET utf8;
    """.format(_random)
    run_sql_mysql(connection_name, sql_create_schema, "", username, _auto_commit)
    return "zyx_schema{}".format(_random)


def create_table_mysql(connection_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    创建mysql 表
    :return:
    """
    _random = random.randint(1000, 9999)
    table_name = "zyx_biao{}".format(_random)
    sql = """CREATE TABLE IF NOT EXISTS `{}`.`{}`
        ( `a` bigint(22) null  COMMENT '备注123XYZ',
         `b` char(22) null  COMMENT '备注123XYZ',
         `c` char(22) null  COMMENT '备注123XYZ',
         `d` date null  COMMENT '备注123XYZ',
         `e` datetime null  COMMENT '备注123XYZ',
         `f` decimal(22) null  COMMENT '备注123XYZ',
         `g` double null  COMMENT '备注123XYZ',
         `h` float(22) null  COMMENT '备注123XYZ',
         `i` int(22) null  COMMENT '备注123XYZ',
          `j` longtext null  COMMENT '备注123XYZ',
         `k` smallint(22) null  COMMENT '备注123XYZ',
         `l` smallint(22) null  COMMENT '备注123XYZ',
         `m` text(22) null  COMMENT '备注123XYZ',
         `n` time(6) null  COMMENT '备注123XYZ',
         `o` timestamp(6) null  COMMENT '备注123XYZ'
        );
    """.format(schema_name, table_name)
    run_sql_mysql(connection_name, sql, schema_name, username, _auto_commit)
    return table_name


def create_schema_and_create_table_mysql(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    先创建schema在创建表
    :return:
    """
    schema_name = create_schema_mysql(connection_name, username, _auto_commit)
    table_name = create_table_mysql(connection_name, schema_name, username, _auto_commit)
    return schema_name, table_name


def create_schema_and_create_table_and_insert_mysql(connection_name="", n=1, username="enmoadmin", _auto_commit=0):
    """
    先创建schema在创建表,在插入数据
    :return:
    """
    schema_name, table_name = create_schema_and_create_table_mysql(connection_name, username, _auto_commit)
    _sql_insert = ["""INSERT INTO `{}`.`{}` VALUES ('1', '33','我的祖国12345', '1999-11-11', '2022-11-11 11:11:11', '999.99', '99.22', '88.12', '65', '', '33', '22', '', '', '2022-11-11 11:11:11');
        """.format(schema_name, table_name)] * int(n)
    run_sql_mysql(connection_name, _sql_insert, schema_name, username, _auto_commit)
    return schema_name, table_name, n


def delete_schema_mysql(connection_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    删除schema
    :return:
    """
    _sql = "DROP DATABASE IF EXISTS `{}`;".format(schema_name)
    run_sql_mysql(connection_name, _sql, "", username, _auto_commit)


def delete_all_schema_mysql(connection_name, schema_name="zyx_schema"):
    """
    删除所有XYZ的schema
    :return:
    """
    _get_all_schema_mysql = get_all_schema_mysql(connection_name)
    # _get_all_schema = []
    for i in _get_all_schema_mysql:
        if schema_name in i:
            # _get_all_schema.append(i)
            delete_schema_mysql(connection_name, i)
    #         # _sql = "DROP USER {} CASCADE".format(i)
    #         # run_sql_oracle(connection_name, _sql)
    #         drive.delete_schema_oracle(i)


def delete_table_mysql(connection_name="", schema_name="", table_name="", username="enmoadmin", _auto_commit=0):
    """
    删除表
    :return:
    """
    _sql = "DROP TABLE IF EXISTS `{}`;".format(table_name)
    run_sql_oracle(connection_name, _sql, schema_name, username, _auto_commit)


# sqlserver操作
def get_all_database_sqlserver(connection_name):
    """
    获取所有database的名称
    :param connection_name:
    :return:
    """
    url = "{}/dms/meta/node".format(base_url)
    connection_id = public.get_connection_id(connection_name)
    payload = {
        "connectionId": connection_id,
        "connectionType": "SQLServer",
        "nodeType": "connection",
        "nodePath": "/root/{}".format(connection_id)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)["data"]
    _node_name_list = [i["nodeName"] for i in res]
    return _node_name_list[:-1]


def run_sql_sqlserver(connection_name="", sql="", x_name="", username="enmoadmin", _auto_commit=0):
    """
    执行sqlserver的SQL语句
    x_name: database的名称
    :return:
    """
    true = True
    false = False
    if int(_auto_commit) == 0:
        auto_commit = true
    else:
        auto_commit = false
    url = "{}/dms/statement/execute".format(config.base_url)
    if type(sql) == str:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "statements": [
                "{}".format(sql).replace(";", "")
            ],
            "segmentIndex": 0,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "SQLServer",
            "operatingObject": "{}".format(x_name),
            "databaseName": "{}".format(x_name),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    elif type(sql) == list:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "statements": sql,
            "segmentIndex": 0,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "SQLServer",
            "operatingObject": "{}".format(x_name),
            "databaseName": "{}".format(x_name),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def create_database_sqlserver(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    创建database
    :return:
    """
    _random = random.randint(1000, 9999)
    sql_create_schema = """CREATE DATABASE zyx_database{};
        """.format(_random)
    run_sql_sqlserver(connection_name, sql_create_schema, "", username, _auto_commit)
    return "zyx_database{}".format(_random)


def create_schema_sqlserver(connection_name="", database="", username="enmoadmin", _auto_commit=0):
    """
    创建 schema
    :return:
    """
    _random = random.randint(1000, 9999)
    sql_create_schema = """CREATE SCHEMA zyx_schema{};
    """.format(_random)
    run_sql_sqlserver(connection_name, sql_create_schema, database, username, _auto_commit)
    return "zyx_schema{}".format(_random)


def create_table_sqlserver(connection_name="", database_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    创建 表
    :return:
    """
    _random = random.randint(1000, 9999)
    table_name = "zyx_biao{}".format(_random)
    sql = """CREATE TABLE [{}].[{}]
    (
         A int    null ,
         B nvarchar(30)    null ,
         C char(20)    null ,
         D nvarchar(100)    null ,
         E nvarchar(30)    null ,
         F nvarchar(100)    null );
    """.format(schema_name, table_name)
    run_sql_sqlserver(connection_name, sql, database_name, username, _auto_commit)
    return table_name


def create_database_and_schema_sqlserver(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    同时创建datbase和schema
    :return:
    """
    _database = create_database_sqlserver(connection_name, username, _auto_commit)
    _schema = create_schema_sqlserver(connection_name, _database, username, _auto_commit)
    return _database, _schema


def create_database_and_schema_and_table_sqlserver(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    同时创建datbase和schema和表
    :param connection_name:
    :param username:
    :param _auto_commit:
    :return:
    """
    _database, _schema = create_database_and_schema_sqlserver(connection_name, username, _auto_commit)
    _table = create_table_sqlserver(connection_name, _database, _schema, username, _auto_commit)
    return _database, _schema, _table


def create_database_and_schema_and_table_and_insert_sqlserver(connection_name="", n=1, username="enmoadmin",
                                                              _auto_commit=0):
    """
    同时创建datbase和schema和表
    :param connection_name:
    :param username:
    :param _auto_commit:
    :return:
    """
    _database, _schema_name, _table_name = create_database_and_schema_and_table_sqlserver(connection_name, username,
                                                                                          _auto_commit)
    _sql_insert = ["""INSERT INTO {}.{}("B","C","D","E","F") VALUES (N'1',N'2',N'人生海海',N'山山而川',N'不过尔尔');
            """.format(_schema_name, _table_name)] * int(n)
    run_sql_sqlserver(connection_name, _sql_insert, _database, username, _auto_commit)
    return _database, _schema_name, _table_name, n


def delete_database_sqlserver(connection_name="", database_name="", username="enmoadmin", _auto_commit=0):
    """
    删除database
    :return:
    """
    _sql = "DROP DATABASE IF EXISTS {}".format(database_name)
    run_sql_sqlserver(connection_name, _sql, "", username, _auto_commit)


def delete_all_database_sqlserver(connection_name="", database_name="zyx_database"):
    """
    删除所有的database
    :return:
    """
    _get_all_database_sqlserver = get_all_database_sqlserver(connection_name)
    for i in _get_all_database_sqlserver:
        if database_name in i:
            print(i)
            delete_database_sqlserver(connection_name, i)


def delete_schema_sqlserver(connection_name="", database_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    删除schema
    :return:
    """
    _sql = "DROP SCHEMA IF EXISTS {};".format(schema_name)
    run_sql_sqlserver(connection_name, _sql, database_name, username, _auto_commit)


def delete_table_sqlserver(connection_name="", database_name="", schema_name="", table_name="", username="enmoadmin",
                           _auto_commit=0):
    """
    删除表
    :return:
    """
    _sql = "DROP TABLE IF EXISTS {}.{};".format(schema_name, table_name)
    run_sql_sqlserver(connection_name, _sql, database_name, username, _auto_commit)


# pg操作
def run_sql_pg(connection_name="", sql="", database_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    执行pg的SQL语句
    :return:
    """
    true = True
    false = False
    if int(_auto_commit) == 0:
        auto_commit = true
    else:
        auto_commit = false
    url = "{}/dms/statement/execute".format(config.base_url)
    if type(sql) == str:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "statements": [
                "{}".format(sql).replace(";", "")
            ],
            "segmentIndex": 0,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "PostgreSQL",
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(database_name),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    elif type(sql) == list:
        payload = {
            "offset": 0,
            "rowCount": 100,
            "statements": sql,
            "segmentIndex": 0,
            "connectionId": get_connection_id(connection_name),
            "dataSourceType": "PostgreSQL",
            "operatingObject": "{}".format(schema_name),
            "databaseName": "{}".format(database_name),
            "tabKey": "{}".format(get_id()),
            "plSql": false,
            "tSql": false,
            "autoCommit": auto_commit
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    return response.text


def create_database_pg(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    创建database
    :return:
    """
    _random = random.randint(1000, 9999)
    sql_create_schema = """CREATE DATABASE zyx_database{} WITH  OWNER = postgres TEMPLATE = template0 ENCODING = 'UTF8';
        """.format(_random)
    run_sql_pg(connection_name, sql_create_schema, "", "", username, _auto_commit)
    return "zyx_database{}".format(_random)


def create_schema_pg(connection_name="", database="", username="enmoadmin", _auto_commit=0):
    """
    创建 schema
    :return:
    """
    _random = random.randint(1000, 9999)
    sql_create_schema = """CREATE SCHEMA zyx_schema{};
    """.format(_random)
    run_sql_pg(connection_name, sql_create_schema, database, "", username, _auto_commit)
    return "zyx_schema{}".format(_random)


def create_table_pg(connection_name="", database_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    创建 表
    :return:
    """
    _random = random.randint(1000, 9999)
    table_name = "zyx_biao{}".format(_random)
    sql = """CREATE TABLE IF NOT EXISTS "{}"."{}"."{}"
    ( "A" text ,
     "B" text ,
     "C" text ,
     "D" text ,
     "E" text ,
     "F" text
    );
    """.format(database_name, schema_name, table_name)
    run_sql_pg(connection_name, sql, "", "", username, _auto_commit)
    return table_name


def create_database_and_schema_pg(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    同时创建datbase和schema
    :return:
    """
    _database = create_database_pg(connection_name, username, _auto_commit)
    _schema = create_schema_pg(connection_name, _database, username, _auto_commit)
    return _database, _schema


def create_database_and_schema_and_table_pg(connection_name="", username="enmoadmin", _auto_commit=0):
    """
    同时创建datbase和schema和表
    :param connection_name:
    :param username:
    :param _auto_commit:
    :return:
    """
    _database, _schema = create_database_and_schema_pg(connection_name, username, _auto_commit)
    _table = create_table_pg(connection_name, _database, _schema, username, _auto_commit)
    return _database, _schema, _table


def create_database_and_schema_and_table_and_insert_pg(connection_name="", n=1, username="enmoadmin",
                                                       _auto_commit=0):
    """
    同时创建datbase和schema和表
    :param connection_name:
    :param username:
    :param _auto_commit:
    :return:
    """
    _database, _schema_name, _table_name = create_database_and_schema_and_table_pg(connection_name, username,
                                                                                   _auto_commit)
    _sql_insert = ["""INSERT INTO "{}"."{}" ("A","B","C","D","E","F") VALUES ('1'::text,'岩下劲松'::text,'少年气'::text,'婉兮清扬'::text,'白昼流星'::text,'来路可期'::text);
            """.format(_schema_name, _table_name)] * int(n)
    run_sql_pg(connection_name, _sql_insert, _database, "", username, _auto_commit)
    return _database, _schema_name, _table_name, n


def delete_database_pg(connection_name="", database_name="", username="enmoadmin", _auto_commit=0):
    """
    删除database
    :return:
    """
    _sql = "DROP DATABASE IF EXISTS {}".format(database_name)
    # print(_sql)
    run_sql_pg(connection_name, _sql, "", "", username, _auto_commit)


def delete_schema_pg(connection_name="", database_name="", schema_name="", username="enmoadmin", _auto_commit=0):
    """
    删除schema
    :return:
    """
    _sql = "DROP SCHEMA IF EXISTS {} CASCADE;".format(schema_name)
    run_sql_pg(connection_name, _sql, database_name, "", username, _auto_commit)


def delete_table_pg(connection_name="", database_name="", schema_name="", table_name="", username="enmoadmin",
                    _auto_commit=0):
    """
    删除表
    :return:
    """
    _sql = 'drop table "{}"."{}"."{}";'.format(database_name, schema_name, table_name)
    run_sql_pg(connection_name, _sql, "", "", username, _auto_commit)


def create_oracle():
    """
    创建oracle数据库连接
    :return:
    """
    _connection_name = "zyx_test{}".format(random.randint(10000, 99999))
    url = "{}/dms/connection/configuration".format(base_url)
    false = False
    headers = {
        'Cookie': '{}'.format(get_cookie("enmoadmin")),
        'Content-Type': 'application/json'
    }
    payload = {
        "dataSourceType": "Oracle",
        "userInputs": {
            "dataSourceVersion": "19c-19.3.0.0.0",
            "connectionName": f"{_connection_name}",
            "connectionUrl": "192.168.3.128",
            "connectionPort": "1521",
            "userName": "sys",
            "password": public.str_to_rsa("123456"),
            "connectionType": "SID",
            "serviceName": "orcl",
            "connectionRole": "SYSDBA",
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "Oracle"
        }
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    if "成功" in response.text:
        return _connection_name
    else:
        return "oracle数据库连接失败"


if __name__ == "__main__":
    # print(create_db_connection("oracle"))
    print(create_all_db_connection())
    # delete_all_schema_oracle("zyx_test1655_oracle")
    # print(create_db_connection("pg"))
    # delete_all_db_connection_name()
    # delete_db_connection_name("zyx_test7943_oracle")
    # _sql = 'insert into "GAOWEI_SCHEMA"."BIAO3333" ("a","b","c") values ("1","1","1")'
    # print(run_sql_oracleCDB("xyz_test6666_oracleCDB", _sql, "gaowei"))
    # for i in range(0, 4000):
    #     print(create_oracle())
    #     print(f"第 {i} 个")
    # print(delete_all_db_connection_name())
    # print(delete_db_connection_name("zyx_test61127"))
    # sql = 'CREATE TABLE "GAOWEI_SCHEMA"."biao26379" ("a" CHAR(22))'
    # print(run_sql_sqlserver("xyz_test6666_SqlServer", sql, "SALESPDB", "gaowei"))
    # print(create_schema_sqlserver("xyz_test6666_SqlServer", "SALESPDB", ))
    # print(get_connection_id("zyx_test2443_PostgreSQL"))
    # delete_db_connection_name("zyx_test3903_DamengDB")
    # print(create_database_pg("zyx_test1654_PostgreSQL"))
    # print(create_all_db_connection())
    # print(run_sql_oracleCDB("zyx_test4738_oracle", 'SELECT * FROM "TB_SCHEMA"."TB_TABLE"', "test44927"))
    # print(run_sql_oracle("zyx_test4738_oracle", 'SELECT * FROM "TB_SCHEMA"."TB_TABLE"', "TB_SCHEMA", "test44927"))
