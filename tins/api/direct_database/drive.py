# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/29'

import cx_Oracle as cx  # 导入模块


# ########################oracle操作########################
def connect_oracle(username='sys', pw='oracle', url='192.168.3.61:1521/xe', role=cx.SYSDBA):
    """
    连接oracle数据库
    :return:
    """
    cx.init_oracle_client(lib_dir='D:/oula/tins/api/direct_database/instantclient_21_3')
    con = cx.connect(username, pw, url, role)  # 创建连接
    return con
    # connection = cx.connect(username, pw, '192.168.3.61:1521/xe', encoding="UTF-8")
    # connection.close()


def delete_schema_oracle(schema_name):
    """
    删除oracle数据源的schame
    :return:
    """
    con = connect_oracle()
    cursor = con.cursor()  # 创建游标
    sql1 = """ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE"""
    sql2 = """DROP USER {} CASCADE""".format(schema_name)
    try:
        cursor.execute(sql1)  # 执行sql语句
        cursor.execute(sql2)
    except:
        pass
    finally:
        cursor.close()  # 关闭游标
        con.close()  # 关闭数据库连接


def delete_all_schema_oracle(all_schema_name_list):
    """
    删除oracle数据源的所有schame
    all_schema_name_list：list列表
    :return:
    """
    con = connect_oracle()
    cursor = con.cursor()  # 创建游标
    sql1 = """ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE"""
    try:
        cursor.execute(sql1)  # 执行sql语句
        for i in all_schema_name_list:
            cursor.execute("""DROP USER {} CASCADE""".format(i))
    except:
        pass
    finally:
        cursor.close()  # 关闭游标
        con.close()  # 关闭数据库连接


if __name__ == '__main__':
    print(connect_oracle())
    # delete_schema_oracle("BASE10")
    # a = ['连接状态（前端维护）', '修改别名', '连接访问提权', '新建查询', 'PL/SQL 编辑器', '打开终端', '连接管理', '编译无效对象', '连接池', '重置连接池', '回收连接池', '移动到组', '复制连接', '复制', '刷新']
    # b = ['连接状态（前端维护）', '修改别名', '连接访问提权', '新建查询', 'PL/SQL 编辑器', '打开终端', '连接管理', '连接池', '重置连接池', '回收连接池', '编译无效对象', '移动到组', '复制连接', '复制', '刷新']
    # print(set(a))
    # print(set(b))