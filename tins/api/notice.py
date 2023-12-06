# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/9'

import jsonpath
import requests
import json
from tins.config import *
import random
import base64
from tins.api.system_management.organization_management import *
from tins.api.flow import apply_flow


def get_notice_info(i=1, ii=10, username="enmoadmin"):
    """
    获取通知首页信息
    :param i: 第一页
    :param ii: 一页展示多少条通知
    :param username:
    :return:
    """
    url = "{}/message/msg/getMessageByUserId/{}/{}".format(base_url, int(i), int(ii))
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


# def get_flow_instance_id():
#     """
#     通过id获取flowInstanceId
#     :return:
#     """
#     _info = get_notice_info()
#     _info = json.loads(_info)


def view_notice(task_id, username="enmoadmin"):
    """
    查看具体通知
    :param username:
    :return:
    """
    url = "{}/api/flow/viewFlowProcess".format(base_url)
    payload = {
        "flowInstanceId": apply_flow.get_flowInstanceId(task_id)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def delete_notice(task_id, username="enmoadmin"):
    """
    删除通知
    :param task_id:即msgId
    :param username:
    :return:
    """
    url = "{}/message/msg/batchDelMessages".format(base_url)
    payload = {
        "ids": [
            int(apply_flow.get_id(task_id))
        ]
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def delete_all_notices(username="enmoadmin"):
    """
    根据用户删除所有通知
    :param msgId
    :param username:
    :return:
    """
    _info = get_notice_info(1, 10000, username)
    _info = json.loads(_info)
    msgId_list = jsonpath.jsonpath(_info, "$.data.data..msgId")
    for i in msgId_list:
        delete_notice(i)


def flow_audit(_id, approvedFlag="yes", username="enmoadmin"):
    """
    对普通用户申请的权限进行做审批，默认审批通过
    :param _id:
    :param approvedFlag:
    :param username:
    :return:
    """
    url = "{}/api/flow/executeFlowTask".format(base_url)
    true = True
    false = False
    if approvedFlag == "yes":
        payload = {
            "flowId": _id,
            "approvedFlag": true,
            "taskId": apply_flow.get_task_id(_id)
        }
    else:
        payload = {
            "flowId": _id,
            "taskId": apply_flow.get_task_id(_id),
            "approvedFlag": false,
            "approvedComment": "中文abc123",
            "approvedTime": ""
        }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
    except:
        print("无此消息通知")


def execute(task_id="", username="enmoadmin"):
    """
    订正提权流程-订正
    :param task_id:
    :param username:
    :return:
    """
    url = "{}/api/flow/{}/execute".format(base_url, task_id)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers)
    return response.text


def rollback(task_id="", username="enmoadmin"):
    """
    订正提权流程-回退
    :param task_id:
    :param username:
    :return:
    """
    url = "{}/api/flow/{}/rollback".format(base_url, task_id)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers)
    return response.text


if __name__ == "__main__":
    execute("86294", "test92726")
    # delete_all_notices()
    # print(get_notice_info(1, 10000))
    # print(flow_audit(1723))
    # print(delete_notice("750"))
    # print(view_notice("87e99e60-a6b1-11ed-a54a-02420a000314"))
