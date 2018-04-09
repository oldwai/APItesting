# encoding: utf-8
"""
@version: python3.5
@author: frank
@contact: frankandrew@163.com
@file: common.py
@time: 2018/4/7 16:49
"""
import base64

'''

common.py定义shopping、pricing、booking过程的公共方法
'''


class CommonMethod:
    def sign_md5(parentID, parentKey):
        import hashlib
        try:
            strings = parentID + parentKey
        except Exception as e:
            print(e)
        m = hashlib.md5()
        m.update(strings.encode(encoding='utf-8'))
        #hexdigest表示加密结果用16进制表示
        return m.hexdigest()

    def para_encryption_base64(para):
        para = str(para)
        # 对字符串进行base64加密时需要先转换为二进制编码
        para_base64 = base64.b64encode(para.encode(encoding="utf-8"))
        # print(type(para_base64))
        return para_base64

    def para_package(self, **kwargs):
        pass

    def get_url(self, host, para):
        pass



if __name__=="__main__":
    # test = CommonMethod()
    pass
