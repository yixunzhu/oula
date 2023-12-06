# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'


import pytest
from tins.api.sdt import sdt_click


def test_001_switch_mode():
    """
    切换模式
    :return:
    """
    _mode = ["light", "dark"]
    for i in _mode:
        res = sdt_click.switch_mode(i)
        assert '{"resCode":10000,"resMsg":"成功","data":null}' == res


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
