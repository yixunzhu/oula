from tins.api.public import *


def home_page(username="enmoadmin"):
    """
    首页
    :param username:
    :return:
    """
    url = f"{base_url}/analyze/operation"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers).status_code
    return response


def all_operate_type(username="enmoadmin"):
    """
    过滤条件：事件类型
    :param username:
    :return:
    """
    url = f"{base_url}/user/users/allOperateType"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def detail(username="enmoadmin"):
    """
    过滤条件：查询
    :param username:
    :return:
    """
    url = f"{base_url}/audit/display/operate_log/detail"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "limit": 10,
        "offset": 0
    })
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


if __name__ == '__main__':
    print(simple_users())
