# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('d:/Github/py-study/')
from PeeweeConn import PeeweeDbConnection as pwDb
from peewee import *
os.environ.setdefault('SETTING', 'lib.settings')
from conf import settings

class BaseModel(Model):

    class Meta():
        database = pwDb.PeeweeDbConnection().getDb(
            dbName=settings.DATABASE_NAME,
            host=settings.DATABASE_HOST,
            port=settings.DATABASE_PORT,
            user=settings.DATABASE_USER,
            pwd=settings.DATABASE_PASSWORD)

class BaseFactory():
    def __init__(self):
        pass
