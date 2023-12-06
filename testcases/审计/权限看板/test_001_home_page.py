# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/7/26'

import pytest
import json
from tins.api.audit import permission_kanban


def test_001_home_page():
    """
    判断首页正常访问
    :param:
    :return:
    """
    assert permission_kanban.home_page() == 200


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
