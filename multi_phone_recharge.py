# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'A multi phone recharge module'

__author__ = 'Gao Yuhao'

import requests
import json
import time
import xlrd
import xlwt

url = "http://p.apix.cn/apixlife/pay/phone/phone_recharge"

querystring = {"phone": "your_value", "price": "your_value", "orderid": "your_value", "sign": "your_value"}
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': ""
}


def md5(str):
    import hashlib
    md = hashlib.md5()
    md.update(str)
    return md.hexdigest()


listbk = xlrd.open_workbook('./list.xls')
list = listbk.sheets()[0]
re = xlwt.Workbook()
relist = re.add_sheet('Result')
relist.write(0, 0, 'phone')
relist.write(0, 1, 'price')
relist.write(0, 2, 'orderid')
relist.write(0, 3, 'sign')
relist.write(0, 4, 'Msg')
relist.write(0, 5, 'Cardname')
headers['apix-key'] = list.cell(0, 3).value

for id in range(list.nrows)[1:]:
    phone = str(int(list.cell(id, 0).value))
    price = str(int(list.cell(id, 1).value))
    querystring['phone'] = phone
    querystring['price'] = price
    querystring['orderid'] = time.strftime('%Y%M%d%H%M%S', time.localtime()) + '%06.0f' % id
    querystring['sign'] = md5(phone + price + querystring['orderid'])
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    #print result   #debug
    relist.write(id, 0, phone)
    relist.write(id, 1, price)
    relist.write(id, 2, querystring['orderid'])
    relist.write(id, 3, querystring['sign'])

    try:
        relist.write(id, 4, result['Msg'])
        relist.write(id, 5, result['Data']['Cardname'])
    except:
        relist.write(id, 4, result['error'])

re.save('./result.xls')
print(u'Job done! 充值结果见result文件，按回车键退出。')
try:
    input()
except:
    pass
