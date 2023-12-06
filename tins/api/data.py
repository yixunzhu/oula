# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/9'


import random

_random = random.randint(10000, 99999)
_create = """
CREATE TABLE "XYZ_SCHEMA_9915"."BIAO{}" ("a" CHAR(22) )
""".format(_random)
_insert = """
insert into "XYZ_SCHEMA_9915"."BIAO" ("a") values ('1')
"""
_delete = """DELETE  BIAO1;"""
_update = """
update "XYZ_SCHEMA_9915"."BIAO" set "a" = '2' where "a" = '1'
"""
_select = 'SELECT * FROM "XYZ_SCHEMA_9915"."BIAO"'
_alter = 'ALTER TABLE "XYZ_SCHEMA_9915"."BIAO4997" ADD "c{}" FLOAT'.format(_random)
_create_index = 'CREATE UNIQUE INDEX  index_name1 ON BIAO{}("a");'.format(_random)
_drop_index = 'DROP INDEX "INDEX_NAME1";'
_create_view = 'CREATE VIEW gg{} as SELECT * FROM "XYZ_SCHEMA_9915"."BIAO";'.format(_random)
