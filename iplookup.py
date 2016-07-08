#! /usr/bin/env python
# -*- coding:utf-8 -*-

'IP查询服务'
from __future__ import unicode_literals
__author__ = 'Gao Yuhao'

import json
import requests
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

print('请输入IP地址:')
ip = {'ip': input()}

url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apikey': "百度API"  # 百度API
}

response = requests.request('get', url, headers=headers, params=ip)

result = json.loads(response.text)
try:
    if result['errMsg'] == 'success':
        country = result['retData']['country']
        province = result['retData']['province']
        city = result['retData']['city']
        district = result['retData']['district']
        carrier = result['retData']['carrier']
        print('所查询IP地址位于 %s,%s,%s,%s; 由%s提供服务.' % (country, province, city, district, carrier))
    else:
        print(result['errMsg'])
except:
    print('请检查IP地址或网络连接!')

try:
    print('按回车键退出')
    input()
except:
    pass
