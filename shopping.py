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
from common.common import CommonMethod

shopping_api_url = 'http://192.168.1.122:8881/shopping2'


class Shopping(CommonMethod):
    def get_url(self):
        pass

    @classmethod
    def shopping(cls, para, host=shopping_api_url):
        print(para)
        para = CommonMethod.para_encryption_base64(para)
        para = para.decode('utf-8')
        url = host + '?param=' + para
        try:
            res = requests.get(url, timeout=30)
        except Exception as e:
            print(e)
        # res = res.json()
        # return res.json()
        return res.text


def shopping(para):
    result = Shopping.shopping(para)
    return result

def search():
    pass


def searchAirLegs():
    pass


def shopping_data_case(authentication, search, request_para=None):
    if request_para is None:
        request_para = {}
    request_para["authentication"] = authentication
    request_para["search"] = search





if __name__ == '__main__':
    parent_id = 'RksVSX7PfZm1yF04adBWYsCD7M4='
    parent_key = 'NjU2OTJiMjAwMTMzY2RkOTg4OWMyY2NkNTg4ODRlOTg='
    ow_data = {
        "authentication": {
            "partnerId": parent_id,
            "sign": CommonMethod.sign_md5(parent_id, parent_key)
        },
        "search": {
            "adults": 1,
            "airline": "QR",
            "children": 0,
            "nonstop": 0,
            "searchAirLegs": [
                {
                    "cabinClass": "Economy",
                    "departureDate": "2018-12-24",
                    "destination": "HEL",
                    "origin": "BJS"
                }
                # },
                # {
                #     "cabinClass": "Economy",
                #     "departureDate": "2018-12-24",
                #     "destination": "MEX",
                #     "origin": "LAX"
                # }
            ]
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
