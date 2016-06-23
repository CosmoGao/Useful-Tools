# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'A recharge check module'

__author__ = 'Gao Yuhao'

import requests
import json

url = "http://p.apix.cn/apixlife/pay/phone/recharge_check"
querystring = {"phone": "phone_num", "price": "price_value"}

print(u'请输入需要查询的手机号码:')
phone_num = input()
print(u'请输入需要查询的金额:')
price_value = input()

querystring['phone'] = '%s' % phone_num
querystring['price'] = '%s' % price_value
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': "2332f0c0cf1c459a490098d876ee1e88"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(json.loads(response.text)['Msg'])

try:
    input()
except:
    pass
