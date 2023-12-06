# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/2/2'

import json
import time
from tins.api import public
from tins.api.public import *
from tins import config
import requests
import random
from tins.api import db_connection_info
from tins.config import *
from tins.api import notice


def get_flow_ui_info(flow_type=1, username="enmoadmin"):
    """
    获取提权界面的信息
    :param username:
    :param flow_type:
    数据订正：1
    数据操作提权：2
    连接访问提权：3
    数据导出提权：4
    数据脱敏提权：5
    高危资源提权：6
    执行次数提权：7
    执行行数提权：8
    UI 提权：9
    :return:
    """
    if flow_type == 1:
        _flow_type = "dataCorrection"
    elif flow_type == 2:
        _flow_type = "dataManipulation"
    elif flow_type == 3:
        _flow_type = "connectionAccess"
    elif flow_type == 4:
        _flow_type = "dataExport"
    elif flow_type == 5:
        _flow_type = "dataMasking"
    elif flow_type == 6:
        _flow_type = "highRisk"
    elif flow_type == 7:
        _flow_type = "executionTimes"
    elif flow_type == 8:
        _flow_type = "executionRows"
    elif flow_type == 9:
        _flow_type = "menuAccess"
    url = "{}/api/flow/connectionList/{}/users/{}".format(base_url, _flow_type, username)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def get_task_id(msg_id):
    """
    根据msg_id获取task_id
    :param msg_id:
    :return:
    """
    try:
        _info = notice.get_notice_info()
        _info = json.loads(_info)
        task_id = jsonpath.jsonpath(_info, "$.data.data[?(@.msgId=={})].flowTaskId".format(msg_id))[0]
        return task_id
    except:
        print("无此消息通知")
        return ""


def get_flowInstanceId(msg_id):
    """
    根据msg_id获取flowInstanceId
    :param msg_id:
    :return:
    """
    try:
        _info = notice.get_notice_info()
        _info = json.loads(_info)
        task_id = jsonpath.jsonpath(_info, "$.data.data[?(@.msgId=={})].flowInstanceId".format(msg_id))[0]
        return task_id
    except:
        print("无此消息通知")
        return ""


def get_id(msg_id):
    """
    根据msg_id获取id
    :param msg_id:
    :return:
    """
    try:
        _info = notice.get_notice_info()
        _info = json.loads(_info)
        _id = jsonpath.jsonpath(_info, "$.data.data[?(@.msgId=={})].id".format(msg_id))[0]
        return _id
    except:
        print("无此消息通知")
        return ""


def connection_access_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin"):
    """
    申请连接访问流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    # 这部分为老的逻辑，自base2.3.8后，就删除了
    # if expiredTimeLimit == "":
    #     expiredTimeLimit_list = [168, 720, 2160, 4320, 8760, 0, random.randint(1, 1000)]
    #     _random_expiredTimeLimit = random.choice(expiredTimeLimit_list)
    # else:
    #     _random_expiredTimeLimit = int(expiredTimeLimit)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        # "expiredTimeLimit": _random_expiredTimeLimit,
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "connectionAccess",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def data_correction_flow(connection_name="", sql1="", sql2="", applyUserId="", firstApproveUserId="enmoadmin",
                         executeType=0):
    """
    申请数据订正流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :return:
    """
    _executeType = "manual" if int(executeType) == 0 else "auto"
    url = "{}/api/flow/apply".format(base_url)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        "flowType": "dataCorrection",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}/ZYX".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "oracleUser",
        "firstApproveUserId": firstApproveUserId,
        "executeText": sql1,
        "executeType": _executeType,
        "rollbackText": sql2
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def data_manipulation_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin"):
    """
    申请数据操作提权流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    # if expiredTimeLimit == "":
    #     expiredTimeLimit_list = [168, 720, 2160, 4320, 8760, 0, random.randint(1, 1000)]
    #     _random_expiredTimeLimit = random.choice(expiredTimeLimit_list)
    # else:
    #     _random_expiredTimeLimit = int(expiredTimeLimit)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        # "expiredTimeLimit": _random_expiredTimeLimit,
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "dataManipulation",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        # "nodePathList": [
        #     "/root/0/{}".format(public.get_connection_id(connection_name))
        # ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId,
        # 新的接口
        "sdtTreeNodes": [{
            "nodeType": "connection",
            "operationList": [
                "Alter",
                "Create_index",
                "Drop",
                "Insert",
                "Select"
            ],
            "nodePathList": [
                "/root/0/{}".format(public.get_connection_id(connection_name))
            ]
        }]
        # 老的接口
        # "operationList": [
        #     "Alter",
        #     "Insert",
        #     "Select",
        #     "Update",
        #     "Create_table",
        #     "Create_index",
        #     "Drop",
        #     "Delete"
        # ]
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def data_export_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin", exportNumLimit=1000):
    """
    申请导出提权流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    默认导出1000行
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "dataExport",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId,
        "exportNumLimit": int(exportNumLimit)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def data_masking_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin"):
    """
    申请数据脱敏提权流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "dataMasking",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def high_risk_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin", operationList=""):
    """
    申请高危提权流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    if operationList == "":
        _operationList = ["Alter", "Insert", "Select", "Update", "Create_table", "Create_index", "Drop", "Delete"]
    else:
        _operationList = operationList
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "highRisk",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId,
        "operationList": _operationList
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def execution_times_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin", executeTimeLimit=1000):
    """
    申请次数提权流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    默认1000次
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "executionTimes",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId,
        "executeTimeLimit": int(executeTimeLimit)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def execution_rows_flow(connection_name="", applyUserId="", firstApproveUserId="enmoadmin", rowNumLimit=1000):
    """
    申请行数提权流程
    :param connection_name: 连接名称
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    默认1000行
    :return:
    """
    url = "{}/api/flow/apply".format(base_url)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文1111",
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "executionRows",
        "connectionId": public.get_connection_id(connection_name),
        "dataSourceType": public.get_data_type(connection_name),
        "nodePathList": [
            "/root/0/{}".format(public.get_connection_id(connection_name))
        ],
        "nodeType": "connection",
        "firstApproveUserId": firstApproveUserId,
        "rowNumLimit": int(rowNumLimit)
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def ui_flow(applyUserId="", firstApproveUserId="", secondApproveUserId="enmoadmin", objName="all"):
    """
    申请UI提权流程
    :param applyUserId: 申请者
    :param firstApproveUserId: 审批者
    :param expiredTimeLimit: 期限
    一周：168；一月：720；三月：2160；半年：4320；一年：8760；永久：0
    自定义：random
    :return:
    """
    if objName == "all" or objName == "ALL" or objName == "All":
        _objName = ["SystemSettings", "ConnectionSettings", "AuditAnalysis"]
    elif int(objName) == 1:
        _objName = ["SystemSettings"]
    elif int(objName) == 2:
        _objName = ["ConnectionSettings"]
    elif int(objName) == 3:
        _objName = ["AuditAnalysis"]
    url = "{}/api/flow/apply".format(base_url)
    payload = {
        "applyUserId": applyUserId,
        "email": "",
        "applyReason": "中文111",
        "beginTime": 1677664800475,
        "endTime": 1777543200475,
        "flowType": "menuAccess",
        "objName": _objName,
        "firstApproveUserId": firstApproveUserId,
        "secondApproveUserId": secondApproveUserId
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': '{}'.format(public.get_cookie(applyUserId)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == '__main__':
    a = data_manipulation_flow("zyx_test4350_oracle", "test39129")
    print(a)
    # print(connection_access_flow("PG", "test002"))
    # print(data_correction_flow("zyx_test4901_oracle", "111", "222", "test002"))
    # print(data_manipulation_flow("PG", "test002"))
    # print(data_export_flow("zyx_test4901_oracle", "test002"))
    # print(get_flow_ui_info("test002",8))
    # print(data_masking_flow("zyx_test4901_oracle", "test002"))
    # print(execution_times_flow("zyx_test4901_oracle", "test002"))
    # print(execution_rows_flow("zyx_test4901_oracle", "test002"))
    # print(connection_access_flow("zyx_test4901_oracle", "test001"))
    # print(get_flowInstanceId(248))
    # _info = connection_access_flow("zyx_test6261_oracle", "test001")
    # _info = json.loads(_info)
    # print(type(_info["data"]), _info["data"])
    # for i in range(3):
    #     a = connection_access_flow("zyx_MaxCompute", "test96584")
    #     print(a)

    # _info = data_manipulation_flow("lxin_mysql", "test001")
    # print(_info)
    # _info = json.loads(_info)
    # _id = _info["data"]
    # notice.flow_audit(_id, "yes")