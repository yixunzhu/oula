# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/6/9'

import jsonpath
import requests
import json
from tins.config import *
import random
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
from base64 import b64decode, b64encode
from tins.api.my_center import version_info
from tins.api.system_management.organization_management import *


def auto_password(password="", _auto=""):
    """
    根据版本号，自动判断是用什么加密方式
    :param password:
    :return:
    """
    _version_info_dict = json.loads(version_info.get_version_info())
    _version_info_str = jsonpath.jsonpath(_version_info_dict, '$..data.versionNumber')[0]
    if _auto == "old":
        _password = pw_to_base64(password)
        return _password
    else:
        if _version_info_str >= "base-2.3.7" or _version_info_str >= "base-2.3.10":
            _password = str_to_rsa(password)
        else:
            _password = pw_to_base64(password)
        return _password


def pw_to_base64(pw):
    """
    明文密码转base64格式的加密
    :return:
    """
    pw = '{}'.format(pw).encode()  # 默认以utf8编码
    res = base64.b64encode(pw)
    return res.decode()  # 默认以utf8解码


def get_public_key():
    """
    备注：base2.3.7版本开始，加密方式改为rsa加密，故先获取public_key
    :return str
    """
    url = "{}/user/sys/transmission/publicKey".format(base_url)
    response = requests.request("GET", url).text
    res = json.loads(response)
    _public_key = jsonpath.jsonpath(res, "$..data.publicKey")
    return _public_key[0]


def str_to_rsa(text: str):
    """"
    明文rsa加密
    :return:str
    """
    _public_key = get_public_key()
    __public_key = b64decode(_public_key)
    rsa_key = RSA.importKey(__public_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)  # 创建用于执行pkcs1_v1_5加密或解密的密码
    cipher_text = base64.b64encode(cipher.encrypt(text.encode('utf-8')))
    _cipher_text = cipher_text.decode('utf-8')
    return _cipher_text


def login(user_id="enmoadmin", password="Hello123$"):
    """
    登录
    默认登录用户和密码：enmoadmin/SGVsbG8xMjMk（Hello123$）
    :param request:
    :return: str/成功
    """
    url = "{}/user/login".format(base_url)
    payload = {
        "userId": "{}".format(user_id),
        "password": "{}".format(str_to_rsa(password))
    }
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    print(res)
    # return jsonpath(json.loads(res), "$.resMsg")[0]


def get_cookie(userId="enmoadmin", password="Hello123$", _auto=""):
    """
    获取cookie
    :return:str
    """
    # _version_info_dict = json.loads(version_info.get_version_info())
    # _version_info_str = jsonpath.jsonpath(_version_info_dict, '$..data.versionNumber')[0]
    # if _version_info_str >= "base-2.3.7" or _version_info_str >= "base-2.3.10":
    #     _password = str_to_rsa(password)
    # else:
    #     _password = pw_to_base64(password)
    url = "{}/user/login".format(base_url)
    payload = {
        "userId": userId,
        # "password": pw_to_base64(password)
        "password": auto_password(password, _auto)
    }
    header = {"Content-Type": "application/json"}
    payload = json.dumps(payload)
    response = requests.request("POST", url, data=payload, headers=header)
    str_cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return "SESSION={}".format(str_cookie["SESSION"])


def create_username(_user_id="", pw="Hello1234%"):
    """
    添加用户，用户名为test?
    默认密码为：Hello1234%
    :return:
    """
    _random = random.randint(10000, 99999)
    url = "{}/user/users".format(base_url)
    user_id = "test{}".format(_random) if _user_id == "" else "{}".format(_user_id)
    payload = {
        "userId": user_id,
        "password": "{}".format(auto_password(pw)),
        "userName": user_id,
        "userGender": "MALE",
        "telephone": "13000000000",
        "dept": "cqUser"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': get_cookie(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if "成功" in response.text or "账号已存在" in response.text:
        return user_id
    else:
        return ""


def update_pw(username, new_pw="Hello123$", old_pw="Hello1234%"):
    """
    修改密码为：Hello123$
    :return:
    """
    _version_info_dict = json.loads(version_info.get_version_info())
    _version_info_str = jsonpath.jsonpath(_version_info_dict, '$..data.versionNumber')[0]
    if _version_info_str >= "base-2.3.7" or _version_info_str >= "base-2.3.10":
        url = "{}/user/users/first/pwd".format(base_url)
        payload = {
            "newPassword": auto_password(new_pw)
        }
        payload = json.dumps(payload)
        headers = {
            'Cookie': '{}'.format(get_cookie(username, old_pw)),
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        if "成功" in response.text:
            return "成功"
        else:
            return "base2.3.7后的版本修改密码失败"
    else:
        url = "{}/user/users/first/pwd/{}".format(base_url, pw_to_base64(new_pw))
        payload = {}
        headers = {
            'Cookie': '{}'.format(get_cookie(username, pw_to_base64(old_pw)))
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        if "成功" in response.text:
            return "成功"
        else:
            return "修改密码失败"


def create_username_and_update_pw(_user_id=""):
    """
    添加用户并重置密码为：Hello123$
    :return:
    """
    username = create_username(_user_id)
    update_pw(username)
    return username


def delete_username(username):
    url = "{}/user/users/{}".format(base_url, username)
    headers = {
        'Cookie': '{}'.format(get_cookie())
    }
    response = requests.request("DELETE", url, headers=headers)
    return response.text


def delete_all_username(username="enmoadmin", _username="test"):
    """
    删除所有用户
    :param username:
    :return:
    """
    _info = get_organization_info(username)
    _info = json.loads(_info)
    user_id = jsonpath.jsonpath(_info, "$.data..userId")
    for i in user_id:
        if _username in i and i != "enmotest" and len(i) > 7:
            delete_username(i)


def get_all_db_connection_name():
    """
    获取所有连接名称
    :return:
    """
    url = "{}/dms/meta/node".format(base_url)
    payload = {
        "nodeType": "root",
        "nodePath": "/root"
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': get_cookie(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)["data"]["data"]
    _db_link_name_list = [i["nodeName"] for i in res]
    return _db_link_name_list[:-1]


def get_info(username="enmoadmin"):
    """
    获取首页所有连接名称信息info
    :return:
    """
    # 原接口
    url = "{}/dms/meta/node".format(base_url)
    # base237修改后的接口
    # url = "{}/dms/connection".format(base_url)
    payload = {
        "nodeType": "root",
        "nodePath": "/root"
    }
    headers = {
        'Cookie': '{}'.format(get_cookie(username)),
        'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    dict_res = json.loads(response.text)
    return dict_res


def get_folder_info(folder_name, username="enmoadmin"):
    """
    获取文件夹信息
    :param folder_name:
    :param username:
    :return:
    """
    group_id = get_group_id(folder_name)
    url = "{}/dms/meta/node".format(base_url)
    payload = {
        "connectionId": 0,
        "nodeType": "connectionGroup",
        "nodeName": folder_name,
        "nodePath": "/root/g-{}".format(group_id),
        "groupId": group_id
    }
    payload = json.dumps(payload)
    headers = {
        'Cookie': get_cookie(username),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def get_unauthorized_info(username="enmoadmin"):
    """
    获取首页所有未授权连接名称信息info
    :return:
    """
    url = "{}/dms/meta/node".format(base_url)
    payload = {
        "connectionId": 0,
        "nodeType": "connectionGroup",
        "nodeName": "未授权组",
        "nodePath": "/root/g--1",
        "groupId": -1
    }
    headers = {
        'Cookie': '{}'.format(get_cookie(username)),
        'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    # return response.text
    dict_res = json.loads(response.text)
    return dict_res


def get_connection_id(connection_name):
    """
    通过连接名称获取connection_id
    :param connection_name:
    :return:
    """
    _info = get_info()
    connection_id = jsonpath.jsonpath(_info, "$.data.data[?(@.nodeName=='{}')].connectionId".format(connection_name))[0]
    return str(connection_id)


def get_group_id(folder_name):
    """
    通过名称文件夹获取group_id
    :param folder_name:
    :return:
    """
    _info = get_info()
    group_id = jsonpath.jsonpath(_info, "$.data.data[?(@.nodeName=='{}')].groupId".format(folder_name))[0]
    return str(group_id)


def get_son_group_id(folder_name, son_folder_name):
    """
    通过名称文件夹获取子文件夹的group_id
    :param folder_name:
    :return:, son_folder_name
    """
    _folder_info = get_folder_info(folder_name)
    _folder_info = json.loads(_folder_info)
    son_group_id = jsonpath.jsonpath(_folder_info, "$.data.data[?(@.nodeName=='{}')].groupId".format(son_folder_name))[
        0]
    return son_group_id


def get_son_group_id_list(folder_name):
    """
    通过名称文件夹获取子文件夹的group_id列表
    :param folder_name:
    :return:, son_folder_name
    """
    _folder_info = get_folder_info(folder_name)
    _folder_info = json.loads(_folder_info)
    son_group_id_list = jsonpath.jsonpath(_folder_info, "$.data.data..groupId")
    if None in son_group_id_list:
        son_group_id_list.remove(None)
    return son_group_id_list


def get_son_folder_name_list(folder_name):
    """
    通过名称文件夹获取子文件夹的名称列表
    :param folder_name:
    :return:, son_folder_name
    """
    _folder_info = get_folder_info(folder_name)
    _folder_info = json.loads(_folder_info)
    son_group_id_list = jsonpath.jsonpath(_folder_info, "$.data.data..nodeName")
    if son_group_id_list:
        return son_group_id_list
    else:
        return ['']


def get_data_type(connection_name):
    """
    根据数据库连接名，或者数据库的类型
    :param connection_name:
    :return:
    """
    _info = get_info()
    _data_type = jsonpath.jsonpath(_info, "$.data.data[?(@.nodeName=='{}')].connectionType".format(connection_name))[0]
    return _data_type


def get_all_db_connection_name1():
    """
    获取所有连接名称
    :return:
    """
    headers = {
        'Content-Type': 'application/json'
    }
    login_data = {
        "userId": "enmoadmin",
        "password": auto_password("Hello123$")
    }
    session = requests.Session()
    session.post(url='http://192.168.3.218/user/login', headers=headers, data=json.dumps(login_data), verify=False)
    # print(login_data)
    # print(res.json())
    payload = {
        "nodeType": "root",
        "nodePath": "/root"
    }
    res = session.post("http://192.168.3.218/dms/meta/node", headers=headers, data=json.dumps(payload))
    print(res.json())


if __name__ == "__main__":
    # print(auto_password())
    # print(pw_to_base64("2023020210580182442"))
    # get_all_db_link_name()
    # print(get_data_type("zyx_test6646_oracle"))
    # print(get_unauthorized_info())
    # print(get_data_type("zyx_test1828_mysql"))
    # print(get_group_id("中文12345"))
    # print(get_all_db_connection_name())
    # print(get_connection_id("zyx_test9473_oracle"))
    print(create_username_and_update_pw("test005"))
    # delete_all_username()
    # _info = get_info()
    # print(type(_info), _info)
    # print(get_cookie())
    # print(create_username_and_update_pw("test011111"))
    # print(create_username())
    # print(get_connection_id("zyx_test9380_MogDB"))
    # print(get_all_db_connection_name())
    # print(str_to_rsa("Hello123$"))
    # print(get_unauthorized_info("test001"))
    # print(create_username())
    # print(update_pw("test88907"))
    # print(auto_password("Hello123$"))
    # print(get_connection_id("lxin_orcl"))
    # print(get_data_type("zyx_test4738_oracle").lower())
    # print(auto_password("Hello123$", "old"))
    # print(create_username_and_update_pw("test20230704_1"))
    # x = 0
    # for i in range(0,500):
    #     x+=1
    #     username = create_username_and_update_pw()
    #     print("添加第{}个用户成功，用户名为：{}".format(x,username ))
    # print(str_to_rsa("Hello123$"))
    # print(login())
    # print(get_all_db_connection_name())
    # print(get_all_db_connection_name1())
    # print(get_data_type("zyx_orcle"))
