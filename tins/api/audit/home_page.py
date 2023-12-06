from tins.api.public import *


def home_page(username="enmoadmin"):
    """
    审计首页
    :param username:
    :return:
    """
    url = f"{base_url}/analyze"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers).status_code
    return response


def sql_execute_amount(username="enmoadmin"):
    """
    首页数据
    :param username:
    :return:
    """
    url = f"{base_url}/audit/display/audit_report/sql_execute_amount"
    payload = json.dumps({
        "days": 7
    })
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def export(username="enmoadmin"):
    """
    导出
    :return:
    """
    url = f"{base_url}/audit/display/audit_report/export_audit_log_sql"
    payload = json.dumps({
        "executeBeginMs": 1690041600000,
        "executeEndMs": 1690387199999,
        "actuatorType": 0,
        "limit": 0,
        "offset": 0
    })
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


if __name__ == '__main__':
    print(export())
