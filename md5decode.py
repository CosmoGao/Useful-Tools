#! /usr/bin/env python
# -*- coding:utf-8 -*-

'MD5解密服务'
from __future__ import unicode_literals
__author__ = 'Gao Yuhao'

import json
import requests
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

print('请输入要解密的MD5:')
md5 = {'md5': input()}

url = 'http://apis.baidu.com/chazhao/md5decod/md5decod'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apikey': "百度API"  # 百度API
}

response = requests.request('get', url, headers=headers, params=md5)

result = json.loads(response.text)

if result['msg'] == 'succeed':
    print('该MD5(%s)的解密结果为:%s' % (result['data']['md5'], result['data']['md5_src']))
else:
    print(result['msg'])

try:
    print('按回车键退出')
    input()
except:
    pass

