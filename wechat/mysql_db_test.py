# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from dbmodel.dbzjw1 import ArticleInfo as AInfo
import json
import re
import time
from datetime import datetime
import requests
from conf import JsonExtention as jsonExt


class DbTest(object):

    def add(self):
        info = {'msg_id':'testmsoijkjyutgaskjd1','title':'zhangjingweiceshide 1','source_url':'httpliksad":kjasdsdsadkj','content_url':'jhiyfdgjfdgj1'}
        res = AInfo.Article.insert(info).execute()
        print(res)

    def get(self):
        pid = 1
        res = AInfo.Article.get_by_id(pid)
        print(json.dumps(res.__dict__, cls=jsonExt.NpEncoder))

def __init__(self):
    pass

if __name__ == "__main__":
    dbt = DbTest()
    #dbt.add()
    dbt.get()