# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from IInterface import IDbConnection as IDbCon
from peewee import *
import datetime

class PeeweeDbConnection(IDbCon.IDbConnection):

    def getDb(self, dbName, host, port, user, pwd):
        '''创建数据库链接'''
        mysqlDb = MySQLDatabase(database=dbName, host=host, port=port, user=user, passwd=pwd)
        mysqlDb.connect()
        return mysqlDb