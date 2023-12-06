# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2021/6/4'

import requests
import json

# 测试
DSJ_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c6f24184-610f-4ad7-82a4-fcf913214386"


def send_message_all(send_message):
    """
    默认发送
    :param send_message:
    :return:
    """
    data = json.dumps({
        "msgtype": "text",
        "text": {
            "content": send_message,  # 发送的消息内容
            "mentioned_list": ['@all']  # 圈出所有人
            # "mentioned_mobile_list": ["19906818917"]
        }
    })

    # 指定机器人发送消息
    requests.post(DSJ_URL, data, auth=('Content-Type', 'application/json'))


def send_projects_xx(send_message, creators):
    """
    默认发送
    :param send_message:
    :return:
    """
    data = json.dumps({
        "msgtype": "text",
        "text": {
            "content": send_message,  # 发送的消息内容
            "mentioned_list": creators  # 圈出所有人
            # "mentioned_mobile_list": ["19906818917"]
        }
    })

    # 指定机器人发送消息
    requests.post(DSJ_URL, data, auth=('Content-Type', 'application/json'))


if __name__ == "__main__":
    send_message_all('abcdefg123')
    # send_projects_xx('abcdefg', ['xiaonian'])
