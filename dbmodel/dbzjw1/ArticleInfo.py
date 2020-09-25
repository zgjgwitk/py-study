# -*- coding: utf-8 -*-
from db.PeeweeConn import MysqlProvider as provider
import datetime
from peewee import *
import abc
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('d:/Github/py-study/')


class Article(provider.BaseModel):
    '''Article表对象'''
    #id = AutoField(primary_key=True)
    msg_id = CharField(max_length=100, default='')
    file_id = CharField()
    title = CharField(max_length=100, default='')
    source_url = CharField(max_length=300, default='')
    content_url = CharField(max_length=300, default='')
    create_time = DateTimeField(default=datetime.datetime.now)
