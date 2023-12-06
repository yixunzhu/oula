# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/3/1'

"""
schema：TB_SCHEMA
biao：TB_TABLE
"""
oracle = {
    'select': 'SELECT * FROM "TB_SCHEMA"."TB_TABLE"',
    'insert': 'insert into "TB_SCHEMA"."TB_TABLE" ("a","b") values ("a","b")',
    'update': 'update "TB_SCHEMA"."TB_TABLE" set "a" = "a","b" = "b" where "a" = "1" and "b" = "1"',
    'delete': 'DELETE TB_TABLE',
    'drop': 'DROP TABLE TB_TABLE1',
    'select_tm': 'SELECT * FROM "TB_SCHEMA"."TB_TUOMIN"',
}

"""
SALESPDB
schema：TB_SCHEMA
biao：TB_TABLE
"""
oraclecdb = {
    'select': 'SELECT * FROM "TB_SCHEMA"."TB_TABLE"',
    'insert': 'insert into "TB_SCHEMA"."TB_TABLE" ("a","b") values ("a","b")',
    'update': 'update "TB_SCHEMA"."TB_TABLE" set "a" = "a","b" = "b" where "a" = "1" and "b" = "1"',
    'delete': 'DELETE TB_TABLE',
    'drop': 'DROP TABLE TB_TABLE1',
    'select_tm': 'SELECT * FROM "TB_SCHEMA"."TB_TUOMIN"'
}

"""
schema：TB_SCHEMA
biao：TB_TABLE
"""
mysql = {
    'select': 'SELECT * FROM `TB_SCHEMA`.`TB_TABLE`',
    'insert': 'insert into `TB_SCHEMA`.`TB_TABLE` (`a`,`b`) values ("a","b")',
    'update': 'update `TB_SCHEMA`.`TB_TABLE` set `a` = "a" where `a` = "a" and `b` = "b"',
    'delete': 'DELETE FROM TB_TABLE',
    'select_tm': 'SELECT * FROM `TB_SCHEMA`.`TB_TUOMIN`'
}

"""
SALESPDB
schema：TB_SCHEMA
biao：TB_TABLE
"""
sqlserver = {
    'select': 'SELECT * FROM TB_SCHEMA.TB_TABLE',
    'insert': """insert into [TB_SCHEMA].[TB_TABLE] ([a],[b]) values ('a','b')""",
    'update': """update [TB_SCHEMA].[TB_TABLE] set [a] = 'a' where [a] = 'aa' and [b] = 'b'""",
    'delete': 'DELETE from TB_SCHEMA.TB_TABLE',
    'select_tm': 'SELECT * FROM TB_SCHEMA.TB_TUOMIN'
}

"""
salespdb
schema：TB_SCHEMA
biao：TB_TABLE
"""
pg = {
    'select': 'SELECT * FROM "TB_SCHEMA"."TB_TABLE"',
    'insert': """insert into "TB_SCHEMA"."TB_TABLE" ("a","b") values ('a'::BPCHAR,'b'::BPCHAR)""",
    'update': """update "TB_SCHEMA"."TB_TABLE" set "a" = 'aa'::BPCHAR,"b" = 'bb'::BPCHAR where "a" = 'a'::BPCHAR and "b" = 'b'::BPCHAR AND ctid in (select ctid from "TB_SCHEMA"."TB_TABLE" where "a" = 'a'::BPCHAR and "b" = 'b'::BPCHAR order by ctid limit 1)""",
    'delete': 'DELETE FROM "TB_SCHEMA"."TB_TABLE"',
    'select_tm': 'SELECT * FROM "TB_SCHEMA"."TB_TUOMIN"',
}
