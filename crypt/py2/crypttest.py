# -*- coding:utf-8 -*- 
# 测试AES加密demo
# for python2
from prpcrypt import *

class crypttest():
    def __init__(self,content):
        self.DBSecretKey = "abcdefghijklmnop" # length = 16
        self.DBIv = "qrstuvwxyz123456" # length = 16
        self.content = content

    def make(self):
        pc = prpcrypt(self.DBSecretKey,self.DBIv)
        e = pc.encrypt(self.content)
        return e

if __name__ == '__main__':
    conn = raw_input("Please intput db connection string:")
    mk = crypttest(conn)
    mk.make()
    print(mk.make())