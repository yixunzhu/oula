# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/11/18'

import json
import time
from tins.api import public
from tins.api import db_sql
from tins.api.public import *
from tins import config
import requests
from tins.api.connection_management import general_configuration
import random
# from tins.api import db_connection_info
from tins.config import *

_connection_name = "zyx_test{}_".format(random.randint(1000, 9999))
# false = "false"
# false = ""
# 这个是老版本的，作废掉
# db_connections_old = {
#     "Oracle": {"version": "19c-19.3.0.0.0",
#                "connection_name": "{}oracle".format(_connection_name),
#                "url": "192.168.3.128",
#                "part": 1521,
#                "username": "sys",
#                "pw": public.str_to_rsa("123456"),  # 明文密码
#                "sid": "SID",
#                "server_name": "orcl",
#                "role": "SYSDBA"
#                },
#     "OracleCDB": {"version": "19c-19.3.0.0.0",
#                   "connection_name": "{}oracleCDB".format(_connection_name),
#                   "url": "192.168.3.128",
#                   "part": 1521,
#                   "username": "sys",
#                   "pw": public.str_to_rsa("123456"),  # 明文密码
#                   "sid": "SID",
#                   "server_name": "orcl",
#                   "role": "SYSDBA"
#                   },
#     "Mysql": {"version": "5.7",
#               "connection_name": "{}mysql".format(_connection_name),
#               "url": "192.168.3.128",
#               "part": "3307",
#               "username": "root",
#               "pw": public.str_to_rsa("root")  # 明文密码
#               },
#     "Damengdb": {"version": "8.0",
#                  "connection_name": "{}DamengDB".format(_connection_name),
#                  "url": "192.168.3.128",
#                  "part": "5236",
#                  "username": "SYSDBA",
#                  "pw": public.str_to_rsa("SYSDBA001")
#                  },
#     "SQLServer": {"version": "2016",
#                   "connection_name": "{}SqlServer".format(_connection_name),
#                   "url": "192.168.3.61",
#                   "part": "2019",
#                   "username": "sa",
#                   "pw": public.str_to_rsa("Hello123$")
#                   },
#     "PostgreSQL": {"version": "11",
#                    "connection_name": "{}PostgreSQL".format(_connection_name),
#                    "url": "cloudquery-postgreSQL",
#                    "part": "5432",
#                    "username": "postgres",
#                    "pw": public.str_to_rsa("Hello123$")
#                    },
#     "MongoDB": {"version": "4.0",
#                 "connection_name": "{}MongoDB".format(_connection_name),
#                 "url": "192.168.3.128",
#                 "part": "27017",
#                 "authDatabase": "admin",
#                 "username": "root",
#                 "pw": public.str_to_rsa("123456")
#                 },
#     "MogDB": {"version": "11",
#               "connection_name": "{}MogDB".format(_connection_name),
#               "url": "192.168.3.128",
#               "part": "6432",
#               "username": "mogdb",
#               "pw": public.str_to_rsa("Enmo@123")
#               },
#     "DB2": {"version": "10.5",
#             "connection_name": "{}DB2".format(_connection_name),
#             "url": "192.168.3.61",
#             "part": "60000",
#             "authDatabase": "testdb2",
#             "username": "db2inst1",
#             "pw": public.str_to_rsa("Hello123456")
#             },
#     "StarRocks": {"version": "2.5",
#                   "connection_name": "{}StarRocks".format(_connection_name),
#                   "url": "192.168.3.72",
#                   "part": "9030",
#                   "username": "root",
#                   "pw": public.str_to_rsa("123456")
#                   }
# }
true = True
false = False
db_connections = {
    "Oracle": {
        "dataSourceType": "Oracle",
        "userInputs": {
            "dataSourceVersion": "19c-19.3.0.0.0",
            "connectionName": "{}oracle".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": 1521,
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
    },
    "OracleCDB": {
        "dataSourceType": "OracleCDB",
        "userInputs": {
            "dataSourceVersion": "19c-19.3.0.0.0",
            "connectionName": "{}oracleCDB".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": 1521,
            "userName": "sys",
            "password": public.str_to_rsa("123456"),
            "connectionType": "SID",
            "serviceName": "orcl",
            "connectionRole": "SYSDBA",
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "OracleCDB"
        }
    },
    "MySQL": {
        "dataSourceType": "MySQL",
        "userInputs": {
            "dataSourceVersion": "5.7",
            "connectionName": "{}mysql".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": "3307",
            "userName": "root",
            "password": public.str_to_rsa("root"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "MySQL"
        }
    },
    "DamengDB": {
        "dataSourceType": "DamengDB",
        "userInputs": {
            "dataSourceVersion": "8.0",
            "connectionName": "{}DamengDB".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": "5236",
            "userName": "SYSDBA",
            "password": public.str_to_rsa("SYSDBA001"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "DamengDB"
        }
    },
    "SQLServer": {
        "dataSourceType": "SQLServer",
        "userInputs": {
            "dataSourceVersion": "2016",
            "connectionName": "{}SqlServer".format(_connection_name),
            "connectionUrl": "192.168.3.61",
            "connectionPort": "2019",
            "userName": "sa",
            "password": public.str_to_rsa("Hello123$"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "SQLServer"
        }
    },
    "PostgreSQL": {
        "dataSourceType": "PostgreSQL",
        "userInputs": {
            "dataSourceVersion": "11",
            "connectionName": "{}PostgreSQL".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": "5432",
            "userName": "postgres",
            "password": public.str_to_rsa("WVCmFZs841@"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "PostgreSQL"
        }
    },
    "MongoDB": {
        "dataSourceType": "MongoDB",
        "userInputs": {
            "dataSourceVersion": "4.0",
            "connectionName": "{}MongoDB".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": "27017",
            "authDatabase": "admin",
            "userName": "root",
            "password": public.str_to_rsa("123456"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "MongoDB"
        }
    },
    "MogDB": {
        "dataSourceType": "MogDB",
        "userInputs": {
            "dataSourceVersion": "11",
            "connectionName": "{}MogDB".format(_connection_name),
            "connectionUrl": "192.168.3.128",
            "connectionPort": "6432",
            "userName": "mogdb",
            "password": public.str_to_rsa("Enmo@123"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "MogDB"
        }
    },
    "DB2": {
        "dataSourceType": "DB2",
        "userInputs": {
            "dataSourceVersion": "11.5",
            "connectionName": "{}DB2".format(_connection_name),
            "connectionUrl": "192.168.3.218",
            "connectionPort": "50000",
            "authDatabase": "dbname",
            "userName": "db2inst1",
            "password": public.str_to_rsa("Hello123$"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "DB2"
        }
    },
    "StarRocks": {
        "dataSourceType": "StarRocks",
        "userInputs": {
            "dataSourceVersion": "2.5",
            "connectionName": "{}StarRocks".format(_connection_name),
            "connectionUrl": "192.168.3.72",
            "connectionPort": "9030",
            "userName": "root",
            "password": public.str_to_rsa("123456"),
            "remark": "",
            "privateConnection": false,
            "devModel": false,
            "dataSourceType": "StarRocks"
        }
    }
}
db_connections_right_click_info = {
    "Oracle": ['修改别名', '新建查询', '打开终端', '连接管理', '编译无效对象', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制',
               '刷新'],
    "OracleCDB": ['修改别名', '新建查询', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "MySQL": ['修改别名', '新建查询', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "DamengDB": ['修改别名', '新建查询', 'PL/SQL 编辑器', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "SQLServer": ['修改别名', '新建查询', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "PostgreSQL": ['修改别名', '新建查询', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "MongoDB": ['修改别名', '新建查询', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "MogDB": ['修改别名', '新建查询', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "DB2": ['修改别名', 'PL/SQL 编辑器', '新建查询', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新'],
    "StarRocks": ['修改别名', '新建查询', '连接管理', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新']
}
db_schema_right_click_info = {
    "Oracle": ['编译无效对象', '复制', '导出', 'SQL', '刷新'],
    "OracleCDB": ['编译无效对象', '复制', '导出', 'SQL', '刷新'],
    "MySQL": ['编辑数据库', '添加数据库', '复制', '导出', 'SQL', '刷新'],
    "DamengDB": ['新建查询', 'PL/SQL 编辑器', '编辑模式', '添加模式', '复制', '导出', 'SQL', '刷新'],
    "SQLServer": ['新建查询', '复制', '刷新'],
    "PostgreSQL": ['新建查询', '添加模式', '复制', '刷新'],
    "MongoDB": [''],
    "MogDB": [''],
    "DB2": ['PL/SQL 编辑器', '新建查询', '添加模式', '导出', 'SQL', '复制', '刷新']
}
db_open_schema_info = {
    "Oracle": ['表', '视图组', '物化视图', '函数组', '存储过程组', '同义词', '序列', '触发器组', '数据库连接', '包', '包体', '任务组'],
    "OracleCDB": ['表', '视图组', '物化视图', '函数组', '存储过程组', '同义词', '序列', '触发器组', '数据库连接', '包', '包体', '任务组'],
    "MySQL": ['表', '视图组', '函数组', '存储过程组'],
    "DamengDB": ['表', '视图组', '存储过程组', '函数组', '物化视图', '同义词', '包', '触发器组'],
    "SQLServer": ['表', '视图组', '函数组', '存储过程组', '序列组', '同义词', '数据库连接'],
    "PostgreSQL": ['表', '外表', '视图', '物化视图', '函数', '存储过程', '序列'],
    "MongoDB": [''],
    "MogDB": ['表', '外表', '视图', '函数', '存储过程', '序列'],
    "DB2": ['表', '视图组', '序列']
}
db_permission = {
    "Oracle": {
        # 25个
        "connection": ["Alter", "Create_table", "Create_index", "Create_view", "Create_sequence", "Create_trigger",
                       "Create_function",
                       "Create_procedure", "Create_package", "Create_package_body", "Create_materialized_view",
                       "Create_job", "Drop",
                       "Delete", "Insert", "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate", "Terminal", "Merge",
                       "Dbconnection_operate",
                       "Execute_anonymous_block", "Compile_invalid_objects", "OtherDDL"],
        # 21个
        "oracleUser": ["Alter", "Create_table", "Create_index", "Create_view", "Create_sequence", "Create_trigger",
                       "Drop", "Create_function",
                       "Create_procedure", "Create_package", "Create_package_body", "Create_materialized_view",
                       "Create_job", "Delete",
                       "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate", "Merge", "Compile_invalid_objects",
                       "Insert"],
        # 10个
        "tableGroup": ["Alter", "Create_table", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                       "Truncate", "Merge"],
        # 9个
        "table": ["Alter", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                  "Truncate", "Merge"]
    },
    "OracleCDB": {
        # 25个
        "connection": ["Alter", "Create_table", "Create_index", "Create_view", "Create_sequence", "Create_trigger",
                       "Create_function",
                       "Create_procedure", "Create_package", "Create_package_body", "Create_materialized_view",
                       "Create_job", "Drop",
                       "Delete", "Insert", "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate", "Terminal", "Merge",
                       "Dbconnection_operate",
                       "Execute_anonymous_block", "Compile_invalid_objects", "OtherDDL"],
        # 21个
        "oracleUser": ["Alter", "Create_table", "Create_index", "Create_view", "Create_sequence", "Create_trigger",
                       "Drop", "Create_function",
                       "Create_procedure", "Create_package", "Create_package_body", "Create_materialized_view",
                       "Create_job", "Delete",
                       "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate", "Merge", "Compile_invalid_objects",
                       "Insert"],
        # 10个
        "tableGroup": ["Alter", "Create_table", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                       "Truncate", "Merge"],
        # 9个
        "table": ["Alter", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                  "Truncate", "Merge"]
    },
    "MySQL": {
        # 20个
        "connection": ["Alter", "Create_database", "Create_table", "Create_index", "Create_view", "Create_function",
                       "Create_procedure", "Create_user", "Drop", "Delete", "Insert", "Select", "Show_view", "Show_db",
                       "Execute(调用函数、存储过程的权限)", "Grant", "Update", "Truncate", "Terminal", "Prepare"],
        # 15个
        "oracleUser": ["Alter", "Create_database", "Create_table", "Create_index", "Create_view", "Create_function",
                       "Create_procedure",
                       "Drop", "Delete", "Insert", "Select", "Show_view", "Execute(调用函数、存储过程的权限)", "Update",
                       "Truncate"],
        # 9个
        "tableGroup": ["Alter", "Create_table", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                       "Truncate"],
        # 8个
        "table": ["Alter", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                  "Truncate"]
    },
    "SQLServer": {
        # 18个
        "connection": ["Alter", "Create_database", "Create_schema", "Create_table", "Create_index", "Create_view",
                       "Create_function", "Create_procedure", "Create_user", "T_SQL", "Drop", "Delete", "Insert",
                       "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate", "Terminal"],
        # 14个
        "database": ["Alter", "Create_schema", "Create_table", "Create_index", "Create_view", "Create_function",
                     "Create_procedure",
                     "Drop", "Delete", "Insert", "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate"],
        # 13个
        "schema": ["Alter", "Create_table", "Create_index", "Create_view", "Create_function", "Create_procedure",
                   "Drop", "Delete",
                   "Insert", "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate"],
        # 9个
        "tableGroup": ["Alter", "Create_table", "Create_index", "Drop", "Delete", "Insert", "Select", "Update",
                       "Truncate"],
        # 9个
        "table": ["Alter", "Create_table", "Create_index", "Drop", "Delete", "Insert", "Select", "Update", "Truncate"]
    },
    "PostgreSQL": {
        # 30个
        "connection": ["Alter", "Create_database", "Create_schema", "Create_table", "Create_index", "Create_view",
                       "Create_materialized_view", "Create_sequence", "Create_function", "Create_procedure",
                       "Create_user", "Create_role",
                       "Create_domain", "Create_conversion", "Create_extension", "Create_server", "Create_user_mapping",
                       "Create_foreign_table", "Create_rule", "Create_text_search", "Create_tablespace", "Set", "Drop",
                       "Delete",
                       "Insert", "Select", "Execute(调用函数、存储过程的权限)", "Update", "Truncate", "Terminal"],
        # 23个
        "database": ["Alter", "Create_schema", "Create_table", "Create_index", "Create_view",
                     "Create_materialized_view",
                     "Create_sequence", "Create_function", "Create_procedure", "Create_domain", "Create_conversion",
                     "Create_extension",
                     "Create_server", "Create_foreign_table", "Create_rule", "Create_text_search", "Drop", "Delete",
                     "Insert", "Select",
                     "Execute(调用函数、存储过程的权限)", "Update", "Truncate"],
        # 20个
        "schema": ["Alter", "Create_table", "Create_index", "Create_view", "Create_materialized_view",
                   "Create_sequence",
                   "Create_function", "Create_procedure", "Create_foreign_table", "Create_domain", "Create_conversion",
                   "Create_rule",
                   "Create_text_search", "Drop", "Delete", "Insert", "Select", "Execute(调用函数、存储过程的权限)", "Update",
                   "Truncate"],
        # 10个
        "tableGroup": ["Alter", "Create_table", "Create_index", "Create_rule", "Drop", "Delete", "Insert", "Select",
                       "Update", "Truncate"],
        # 9个
        "table": ["Alter", "Create_index", "Create_rule", "Drop", "Delete", "Insert", "Select",
                  "Update", "Truncate"]
    },
}


def is_db_connection(db):
    """
    数据源是否连接成功
    :return:
    """
    url = "{}/dms/connection/effectiveness".format(config.base_url)
    headers = {
        'Cookie': '{}'.format(public.get_cookie()),
        'Content-Type': 'application/json'
    }
    if db.lower() in "oracle" and db.lower() not in "oraclecdb":
        payload = db_connections["Oracle"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "oraclecdb":
        payload = db_connections["OracleCDB"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "mysql":
        payload = db_connections["MySQL"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "sqlserver":
        payload = db_connections["SQLServer"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "damengdb":
        payload = db_connections["DamengDB"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "postgresql" or db.lower() in "pg":
        payload = db_connections["PostgreSQL"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "mongodb":
        payload = db_connections["MongoDB"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "mogdb":
        payload = db_connections["MogDB"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "db2":
        payload = db_connections["DB2"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False
    elif db.lower() in "starrocks":
        payload = db_connections["StarRocks"]
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        if "成功" in response.text:
            return True
        else:
            return False


def is_all_dbs_connection():
    db_list = list(db_connections.keys())
    _title = ""
    for i in db_list:
        _title += "{}连接状态：{};".format(i, is_db_connection(i))
    return _title


def assert_db_permission(connection_name):
    """
    校验数据源的各层级的权限有无变动
    :param connection_name:
    :return:
    """
    connection_id = get_connection_id(connection_name)
    _data_type = get_data_type(connection_name)
    url = "{}/user/permission/datasource".format(config.base_url)
    # node_type = list(db_permission[_data_type].keys())
    for k, v in db_permission[_data_type].items():
        payload = {
            "connectionId": connection_id,
            "dataSourceType": _data_type,
            "nodeType": k
        }
        payload = json.dumps(payload)
        headers = {
            'Cookie': '{}'.format(public.get_cookie()),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(response.text)
        v_list = [ii["opName"] for ii in res["data"]]
        if set(v_list) != set(v):
            print("数据源{}的{}分层权限和之前有变动为：{}".format(_data_type, k, list(set(v_list) - set(v))))


def assert_all_db_permission():
    _db_type = list(db_permission.keys())
    db_connection_name_list = []
    for i in _db_type:
        db_connection_name = db_sql.create_db_connection(i)
        db_connection_name_list.append(db_connection_name)
    for ii in db_connection_name_list:
        assert_db_permission(ii)
        # db_sql.dele


if __name__ == "__main__":
    # assert_db_permission("zyx_test4265_mysql")
    # assert_all_db_permission()
    # print(assert_db_permission("zyx_test8097_oracle"))
    # assert_all_db_permission()
    # print(is_all_dbs_connection())
    # print(is_db_connection("oracle"))
    # a = db_connections.keys()
    # print(list(a))
    # a = ['Oracle', 'OracleCDB', 'Mysql', 'Damengdb', 'SQLServer', 'PostgreSQL', 'MongoDB', 'MogDB', 'DB2', 'StarRocks']
    # b = eval(str(a).lower())
    # print(a, b)
    # # print("oracle" in a)
    # print(is_all_dbs_connection())
    print(is_db_connection("oracle"))
