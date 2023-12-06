# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/9'

import random

_random = random.randint(10000, 99999)

permission_data = {
    'Oracle': {
        'connection': ['Alter', 'Create_table', 'Create_index', 'Create_view', 'Create_sequence', 'Create_trigger',
                       'Create_function', 'Create_procedure', 'Create_package', 'Create_package_body',
                       'Create_materialized_view', 'Create_job', 'Drop', 'Delete', 'Insert', 'Execute', 'Update',
                       'Truncate', 'Merge', 'Dblink_operate', 'Execute_anonymous_block', 'Compile_invalid_objects',
                       'OtherDDL'],
        'oracleUser': ['Alter', 'Create_table', 'Create_index', 'Create_view', 'Create_sequence', 'Create_trigger',
                       'Drop', 'Create_function', 'Create_procedure', 'Create_package', 'Create_package_body',
                       'Create_materialized_view', 'Create_job', 'Delete', 'Insert', 'Execute', 'Update', 'Truncate',
                       'Merge', 'Compile_invalid_objects', 'OtherDDL'],
        'tableGroup': ['Alter', 'Create_table', 'Create_index', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate',
                       'Merge'],
        'table': ['Alter', 'Create_index', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate', 'Merge'],
        'column': ['Insert', 'Update']
    },
    'MySQL': {
        'connection': ['Alter', 'Create_database', 'Create_table', 'Create_index', 'Create_view', 'Create_function',
                       'Create_procedure', 'Create_user', 'Drop', 'Delete', 'Insert', 'Show_view', 'Show_db', 'Execute',
                       'Grant', 'Update', 'Truncate', 'Prepare'],
        'database': ['Alter', 'Create_database', 'Create_table', 'Create_index', 'Create_view', 'Create_function',
                     'Create_procedure', 'Drop', 'Delete', 'Insert', 'Show_view', 'Execute', 'Update', 'Truncate'],
        'tableGroup': ['Alter', 'Create_table', 'Create_index', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate'],
        'table': ['Alter', 'Create_index', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate'],
        'column': ['Insert', 'Update']
    },
    'PostGreSQL': {
        'connection': ['Alter', 'Create_database', 'Create_schema', 'Create_table', 'Create_index', 'Create_view',
                       'Create_materialized_view', 'Create_sequence', 'Create_function', 'Create_procedure',
                       'Create_user', 'Create_role', 'Create_domain', 'Create_conversion', 'Create_extension',
                       'Create_server', 'Create_user_mapping', 'Create_foreign_table', 'Create_rule',
                       'Create_text_search', 'Create_tablespace', 'Set', 'Drop', 'Delete', 'Insert', 'Execute',
                       'Update', 'Truncate'],
        'database': ['Alter', 'Create_schema', 'Create_table', 'Create_index', 'Create_view',
                     'Create_materialized_view', 'Create_sequence', 'Create_function', 'Create_procedure',
                     'Create_domain', 'Create_conversion', 'Create_extension', 'Create_server', 'Create_foreign_table',
                     'Create_rule', 'Create_text_search', 'Drop', 'Delete', 'Insert', 'Execute', 'Update', 'Truncate'],
        'schema': ['Alter', 'Create_table', 'Create_index', 'Create_view', 'Create_materialized_view',
                   'Create_sequence', 'Create_function', 'Create_procedure', 'Create_foreign_table', 'Create_domain',
                   'Create_conversion', 'Create_rule', 'Create_text_search', 'Drop', 'Delete', 'Insert', 'Execute',
                   'Update', 'Truncate'],
        'tableGroup': ['Alter', 'Create_table', 'Create_index', 'Create_rule', 'Drop', 'Delete', 'Insert', 'Update',
                       'Truncate'],
        'table': ['Alter', 'Create_index', 'Create_rule', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate'],
        'column': ['Insert', 'Update']
    },
    'SQLServer': {
        'connection': ['Alter', 'Create_database', 'Create_schema', 'Create_table', 'Create_index', 'Create_view',
                       'Create_function', 'Create_procedure', 'Create_user', 'T_SQL', 'Drop', 'Delete', 'Insert',
                       'Execute', 'Update', 'Truncate'],
        'database': ['Alter', 'Create_schema', 'Create_table', 'Create_index', 'Create_view', 'Create_function',
                     'Create_procedure', 'Drop', 'Delete', 'Insert', 'Execute', 'Update', 'Truncate'],
        'schema': ['Alter', 'Create_table', 'Create_index', 'Create_view', 'Create_function', 'Create_procedure',
                   'Drop', 'Delete', 'Insert', 'Execute', 'Update', 'Truncate'],
        'tableGroup': ['Alter', 'Create_table', 'Create_index', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate'],
        'table': ['Alter', 'Create_table', 'Create_index', 'Drop', 'Delete', 'Insert', 'Update', 'Truncate'],
        'column': ['Insert', 'Update']
    },
    'OracleCDB': {
        'materializedView': ['Alter', 'Drop'],
        'sequenceGroup': ['Create_sequence', 'Alter', 'Drop'],
        'sequence': ['Alter', 'Drop'],
        'jobsGroup': ['Create_job', 'Alter'],
        'dbLinkGroup': ['Create_dblink', 'Alter', 'Drop', 'Dblink_operate'],
        'dbLink': ['Alter', 'Drop', 'Dblink_operate']
    }

}
# ################################oracle操作################################
_create_table_sql = 'CREATE TABLE "GAOWEI_SCHEMA"."biao{}" ("a" CHAR(22))'.format(_random)
_insert_sql = 'insert into "GAOWEI_SCHEMA"."BIAO3333" ("a") values ("2")'
_updata_sql = 'update "GAOWEI_SCHEMA"."BIAO3333" set "a" = "22" where "a" = "2"'
_delete_sql = 'delete from "GAOWEI_SCHEMA"."BIAO3333" where "a" = "22"'
_alter_sql = 'ALTER TABLE "GAOWEI_SCHEMA"."BIAO3333" ADD "c" FLOAT'
oracle_connection_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracle_oracleUser_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracle_tableGroup_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracle_table_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracle_column_sql = {
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
}
# ################################oracleCDB操作################################
_create_table_sql = 'CREATE TABLE "GAOWEI_SCHEMA"."biao{}" ("a" CHAR(22))'.format(_random)
_insert_sql = 'insert into "GAOWEI_SCHEMA"."BIAO3333" ("a","b","c") values ("1","1","1")'
_updata_sql = 'update "GAOWEI_SCHEMA"."BIAO3333" set "a" = "22" where "a" = "2"'
_delete_sql = 'delete from "GAOWEI_SCHEMA"."BIAO3333" where "a" = "22"'
_alter_sql = 'ALTER TABLE "GAOWEI_SCHEMA"."BIAO3333" ADD "c" FLOAT'
oracleCDB_connection_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracleCDB_oracleUser_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracleCDB_database_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracleCDB_tableGroup_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracleCDB_table_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
oracleCDB_column_sql = {
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
}
# ################################mysql操作################################
_create_table_sql = 'CREATE TABLE "GAOWEI_SCHEMA"."biao{}" ("a" CHAR(22))'.format(_random)
_insert_sql = 'insert into "GAOWEI_SCHEMA"."BIAO3333" ("a") values ("2")'
_updata_sql = 'update "GAOWEI_SCHEMA"."BIAO3333" set "a" = "22" where "a" = "2"'
_delete_sql = 'delete from "GAOWEI_SCHEMA"."BIAO3333" where "a" = "22"'
_alter_sql = 'ALTER TABLE "GAOWEI_SCHEMA"."BIAO3333" ADD "c" FLOAT'
mysql_connection_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
mysql_oracleUser_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
mysql_tableGroup_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
mysql_table_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
mysql_column_sql = {
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
}
# ################################PG操作################################
_create_table_sql = 'CREATE TABLE "GAOWEI_SCHEMA"."biao{}" ("a" CHAR(22))'.format(_random)
_insert_sql = 'insert into "GAOWEI_SCHEMA"."BIAO3333" ("a") values ("2")'
_updata_sql = 'update "GAOWEI_SCHEMA"."BIAO3333" set "a" = "22" where "a" = "2"'
_delete_sql = 'delete from "GAOWEI_SCHEMA"."BIAO3333" where "a" = "22"'
_alter_sql = 'ALTER TABLE "GAOWEI_SCHEMA"."BIAO3333" ADD "c" FLOAT'
pg_connection_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
pg_oracleUser_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
pg_database_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
pg_tableGroup_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
pg_table_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
pg_column_sql = {
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
}
# ################################SqlServer操作################################
_create_table_sql = 'CREATE TABLE "GAOWEI_SCHEMA"."biao{}" ("a" CHAR(22))'.format(_random)
_insert_sql = 'insert into "GAOWEI_SCHEMA"."BIAO3333" ("a") values ("2")'
_updata_sql = 'update "GAOWEI_SCHEMA"."BIAO3333" set "a" = "22" where "a" = "2"'
_delete_sql = 'delete from "GAOWEI_SCHEMA"."BIAO3333" where "a" = "22"'
_alter_sql = 'ALTER TABLE "GAOWEI_SCHEMA"."BIAO3333" ADD "c" FLOAT'
sqlserver_connection_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
sqlserver_oracleUser_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
sqlserver_database_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
sqlserver_tableGroup_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
sqlserver_table_sql = {
    'create_table_sql': _create_table_sql,
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
    'delete_sql': _delete_sql,
    'alter_sql': _alter_sql
}
sqlserver_column_sql = {
    'insert_sql': _insert_sql,
    'updata_sql': _updata_sql,
}
