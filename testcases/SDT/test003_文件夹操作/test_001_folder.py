# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api.sdt import sdt_click
import jsonpath
import json
import random
from tins.api import public


def test_001_new_folder_and_delete_folder():
    """
    新建并删除文件夹
    :return:
    """
    _folder_name = sdt_click.new_folder()
    res = sdt_click.delete_folder(_folder_name)
    assert "成功" in res


def test_002_right_folder():
    """
    右键文件夹
    :return:
    """
    _folder_name = sdt_click.new_folder()
    res = sdt_click.sdt_folder_right_click(_folder_name)
    res = json.loads(res)
    _list = jsonpath.jsonpath(res, "$.data..menuName")
    sdt_click.delete_folder(_folder_name)
    assert ['重命名', '删除组', '新建子组', '复制', '刷新'] == _list


def test_003_rename_folder():
    """
    重命名文件夹
    :return:
    """
    _random = random.randint(1000, 9999)
    _folder_name = sdt_click.new_folder()
    new_folder = sdt_click.rename_folder(_folder_name, _folder_name+str(_random))
    _folder_list = public.get_all_db_connection_name()
    sdt_click.delete_folder(new_folder)
    assert new_folder in _folder_list


def test_004_new_son_folder():
    """
    新建子文件夹
    :return:
    """
    _folder_name = sdt_click.new_folder()
    _new_son_folder = sdt_click.new_son_folder(_folder_name)
    _get_info = public.get_info()
    _get_folder_info = public.get_folder_info(_folder_name)
    # 先删子文件夹，后删父文件夹
    public.get_son_group_id(_folder_name, _new_son_folder)
    public.get_group_id(_folder_name)
    sdt_click.delete_son_folder(_folder_name, _new_son_folder)
    sdt_click.delete_folder(_folder_name)
    assert _folder_name in str(_get_info)
    assert _new_son_folder in _get_folder_info


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
    # print(test_004_new_son_folder())
