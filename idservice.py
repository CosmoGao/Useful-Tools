#! /usr/bin/env python
# -*- coding:utf-8 -*-

'身份证核验服务'

__author__ = 'Gao Yuhao'

import json
import requests

print(u'请输入身份证号:')
id = {'id': raw_input()}

url = 'http://apis.baidu.com/apistore/idservice/id'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apikey': "2618b6917b8f2cad138bf718caaae30b"  # 百度API
}

response = requests.request('get', url, headers=headers, params=id)

result = json.loads(response.text)

if result['retMsg'] == 'success':
    if result['retData']['sex'] == "M":
        sex = u'男'
    else:
        sex = u'女'
    print(u"所查询身份证为" + result['retData']['birthday'] + u'于' + result['retData']['address'] + u'出生的%s性' % sex)
else:
    print(result['retMsg'])
try:
    print(u'按回车键退出')
    input()
except:
    pass
