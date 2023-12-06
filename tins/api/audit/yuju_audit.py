from tins.api.public import *


def home_page(username="enmoadmin"):
    """
    首页
    :param username:
    :return:
    """
    url = f"{base_url}/analyze/execution"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers).status_code
    return response


def toolbar(username="enmoadmin"):
    """
    数据源类型下拉框
    :return:
    """
    url = f"{base_url}/dms/connection/toolbar"
    payload = json.dumps({
        "nodeType": "root"
    })
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def find_audit_log(username="enmoadmin"):
    """
    查询功能
    :param username:
    :return:
    """
    url = f"{base_url}/audit/display/audit_report/find_audit_log"
    payload = json.dumps({
        "actuatorType": 0,
        "limit": 10,
        "offset": 0
    })
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def simple_users(username="enmoadmin"):
    """
    过滤条件：用户
    :param username:
    :return:
    """
    url = f"{base_url}/user/users/simpleUsers"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def datasource_list(username="enmoadmin"):
    """
    过滤条件：数据源类型
    :param username:
    :return:
    """
    url = f"{base_url}/dms/meta/datasource_list"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def find_server_ip(username="enmoadmin"):
    """
    过滤条件：请选择主机
    :param username:
    :return:
    """
    url = f"{base_url}/audit/display/openapi/find_server_ip"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


if __name__ == '__main__':
    print(find_audit_log())
