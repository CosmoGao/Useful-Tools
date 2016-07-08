#! /usr/bin/env python
# -*- coding:utf-8 -*-

'身份证核验服务'
from __future__ import unicode_literals
__author__ = 'Gao Yuhao'

import json
import requests
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

print('请输入身份证号:')
id = {'id': input()}

url = 'http://apis.baidu.com/apistore/idservice/id'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apikey': "百度API"  # 百度API
}

response = requests.request('get', url, headers=headers, params=id)

result = json.loads(response.text)

if result['retMsg'] == 'success':
    if result['retData']['sex'] == "M":
        sex = '男'
    else:
        sex = '女'
    print("所查询身份证为" + result['retData']['birthday'] + '于' + result['retData']['address'] + '出生的%s性' % sex)
else:
    print(result['retMsg'])
try:
    print('按回车键退出')
    input()
except:
    pass
