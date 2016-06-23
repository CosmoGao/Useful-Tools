#! /usr/bin/env python
# -*- coding:utf-8 -*-

'短链接'

__author__ = 'Gao Yuhao'

import json
import requests

url_long = raw_input(u'请输入要转换的长连接:'.encode('gbk'))

if url_long[:6] == 'http://' or url_long[:7] == 'https://':
    url_long = url_long
else:
    url_long = 'http://' + url_long

link = {
    'source': '5786724301'
    , 'url_long': url_long
}

url = 'http://api.weibo.com/2/short_url/shorten.json'

headers = {
    'accept': "application/json",
    'content-type': "application/json",
}

response = requests.request('get', url, headers=headers, params=link)

result = json.loads(response.text)

try:
    print(u'短链接地址为:' + result[u'urls'][0][u'url_short'])
except:
    print(u'生成短链接失败，请检查输入或网络连接。')

try:
    if raw_input(u'按回车键退出'.encode('gbk')) == '?':
        print(result)
    else:
        pass
except:
    pass
