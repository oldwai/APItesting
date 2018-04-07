# encoding: utf-8
"""
@version: python3.5
@author: frank
@contact: frankandrew@163.com
@file: tongcheng_API.py
@time: 2018/3/21 17:59
"""
import base64

import requests
import time
from APItesting.common.common import CommonMethod


class Shopping(CommonMethod):
    def get_url(self):

    def shopping(self, para, host='http://192.168.1.122:8881/shopping2'):
        print(para)
        para = para_encryption_base64(para)
        para = para.decode('utf-8')
        url = host + '?param=' + para
        try:
            res = requests.get(url, timeout=30)
        except Exception as e:
            print(e)
        # res = res.json()
        return res.text


if __name__ == '__main__':
    parentid = 'RksVSX7PfZm1yF04adBWYsCD7M4='
    parentkey = 'NjU2OTJiMjAwMTMzY2RkOTg4OWMyY2NkNTg4ODRlOTg='
    ow_data = {
        "authentication": {
            "partnerId": parentid,
            "sign": sign_md5(parentid, parentkey)
        },
        "search": {
            "adults": 1,
            "airline": "",
            "children": 0,
            "nonstop": 1,
            "searchAirLegs": [
                {
                    "cabinClass": "Economy",
                    "departureDate": "2018-04-27",
                    "destination": "MEL",
                    "origin": "HKG"
                }
            ],
            "solutions": 20
        }
    }
    jounarys = shopping(ow_data)
    print(jounarys)
    # for i in range(1,31):
    #     res = shopping(ow_data)
    #     journeys = len(res['data']['journeys'])
    #     print(res['data']['journeys'])
    #     if journeys:
    #         break
    #     else:
    #         print('第 %d 次'%i)
    #         time.sleep(0.5)

    # sign = sign_md5(parentid, parentkey)
    # print(sign)
