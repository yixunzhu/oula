# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2022/5/10'


import requests
import json
import pytest
from tins import config
from tins.api import public


def test_001():
    url = "{}/dms/segment/statement/execute".format(config.base_url)
    false = False
    payload = {
          "offset": 0,
          "rowCount": 100,
          "statements": [
            "SELECT * FROM \"SYS\".\"ACCESS$\""
          ],
          "segmentIndex": 0,
          "connectionId": 35,
          "dataSourceType": "Oracle",
          "operatingObject": "SYS",
          "databaseName": "SYS",
          "tabKey": "2fa3fbf5-29b6-4c37-888e-8db8bd4f332f",
          "plSql": false,
          "tSql": false
        }
    headers = {
        'Cookie': public.get_cookie(),
        'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.loads(response.content)

    assert result['resMsg'] == "成功"


if __name__ == '__main__':
    pytest.main(args=[__file__, "-s"])
