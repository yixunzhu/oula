# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/11'

import pytest
from tins.api import notice
import json
import jsonpath
import random


def test_001_get_notice_info():
    """
    查看通知页面
    :return:
    """
    _info = notice.get_notice_info()
    _info = json.loads(_info)
    res_msg = "".join(jsonpath.jsonpath(_info, "$.resMsg"))
    total = jsonpath.jsonpath(_info, "$.data.total")
    assert res_msg == "成功"
    assert total[0] >= 0


def test_002_view_notice():
    """
    随机查看通知
    :return:
    """
    _info = notice.get_notice_info()
    _info = json.loads(_info)
    total = jsonpath.jsonpath(_info, "$.data.total")
    # flow_instance_id_list = jsonpath.jsonpath(_info, "$.data.data..flowInstanceId")
    msgId_list = jsonpath.jsonpath(_info, "$.data.data..msgId")
    if total[0] > 0:
        _random = random.randint(0, len(msgId_list))
        # flow_instance_id = flow_instance_id_list[_random]
        msgId = msgId_list[_random]
        _res = notice.view_notice(msgId)
        _res = json.loads(_res)
        res_msg = "".join(jsonpath.jsonpath(_res, "$.resMsg"))
        total = jsonpath.jsonpath(_info, "$.data")
        assert res_msg == "成功"
        assert len(total[0]) >= 0


def test_003_delete_notice():
    """
    随机删除通知
    :return:
    """
    _info = notice.get_notice_info()
    _info = json.loads(_info)
    total = jsonpath.jsonpath(_info, "$.data.total")
    _msgId_list = jsonpath.jsonpath(_info, "$.data.data..msgId")
    if total[0] > 0:
        _random = random.randint(0, len(_msgId_list)-1)
        _id = _msgId_list[_random]
        _res = notice.delete_notice(_id)
        _res = json.loads(_res)
        res_msg = "".join(jsonpath.jsonpath(_res, "$.resMsg"))
        _info = notice.get_notice_info()
        _info = json.loads(_info)
        _id_list = jsonpath.jsonpath(_info, "$.data.data..id")
        assert res_msg == "成功"
        assert _id not in _id_list


if __name__ == "__main__":
    pytest.main(args=[__file__, "-s"])
