from tins.api.public import *


def home_page(username="enmoadmin"):
    """
    首页
    :param username:
    :return:
    """
    url = f"{base_url}/dashboard"
    headers = {
        'Cookie': '{}'.format(public.get_cookie(username)),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers).status_code
    return response


if __name__ == '__main__':
    print(home_page())