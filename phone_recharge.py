# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'A phone recharge module'

__author__ = 'Gao Yuhao'

import requests
import json
import time

url = "http://p.apix.cn/apixlife/pay/phone/phone_recharge"

querystring = {"phone": "your_value", "price": "your_value", "orderid": "your_value", "sign": "your_value"}

print(u'请输入需要充值的手机号码:')
phone_num = raw_input()
print(u'请输入需要充值的金额:')
price_value = raw_input()


def md5(str):
    import hashlib
    md = hashlib.md5()
    md.update(str)
    return md.hexdigest()


querystring['phone'] = '%s' % phone_num
querystring['price'] = '%s' % price_value
querystring['orderid'] = time.strftime('%Y%m%d%H%M%S', time.localtime()) + '000000'
querystring['sign'] = md5(phone_num + price_value + querystring['orderid'])

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': "2332f0c0cf1c459a490098d876ee1e88"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(json.loads(response.text)['Msg'])
print(json.loads(response.text))
try:
    input()
except:
    pass
