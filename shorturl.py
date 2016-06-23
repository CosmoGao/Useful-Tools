#! /usr/bin/env python
# -*- coding:utf-8 -*-

'短链接'

__author__ = 'Gao Yuhao'

import json
import requests

url = 'http://apis.baidu.com/chazhao/shorturl/shorturl'

headers = {
    'accept': "application/json;charset=utf-8",
    'content-type': "application/json;charset=utf-8",
    'apikey': "2618b6917b8f2cad138bf718caaae30b"    #百度API
}

link = {'type':1,'url':['http://www.163.com','http://www.163.com']}


response = requests.post( url, headers=headers, data=link)

result = json.loads(response.text)
print result


try:
    input(u'按回车键退出')
except:
    pass
