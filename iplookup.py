#! /usr/bin/env python
# -*- coding:utf-8 -*-

'IP查询服务'

__author__ = 'Gao Yuhao'

import json
import requests

ip = {'ip': raw_input('请输入IP地址:')}

url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apikey': "API"  # 百度API
}

response = requests.request('get', url, headers=headers, params=ip)

result = json.loads(response.text)

if result['errMsg'] == 'success':
    country = result['retData']['country']
    province = result['retData']['province']
    city = result['retData']['city']
    district = result['retData']['district']
    carrier = result['retData']['carrier']
    print(u'所查询IP地址位于 %s,%s,%s,%s; 由%s提供服务.' % (country, province, city, district, carrier))
else:
    print(result['errMsg'])
try:
    input(u'按回车键退出')
except:
    pass
