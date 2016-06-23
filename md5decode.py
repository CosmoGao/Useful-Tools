#! /usr/bin/env python
# -*- coding:utf-8 -*-

'MD5解密服务'

__author__ = 'Gao Yuhao'

import json
import requests

md5 = {'md5': raw_input('请输入要解密的MD5:'.encode('gbk'))}

url = 'http://apis.baidu.com/chazhao/md5decod/md5decod'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apikey': "API"  # 百度API
}

response = requests.request('get', url, headers=headers, params=md5)

result = json.loads(response.text)

if result['msg'] == 'succeed':
    print(u'该MD5(%s)的解密结果为:%s' % (result['data']['md5'], result['data']['md5_src']))
else:
    print(result['msg'])

try:
    input(u'按回车键退出'.encode('gbk'))
except:
    pass
