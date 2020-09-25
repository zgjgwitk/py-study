# -*- coding: utf-8 -*-
import json  
from datetime import date, datetime
import numpy as np
from numpyencoder import NumpyEncoder
  
class NpEncoder(json.JSONEncoder):
    '''对象序列化为json字符串，处理特殊类型不能转换的情况，否则会抛出异常：Object of type xxx is not JSON serializable

    使用方法为：``json.dumps(res.__dict__, cls=jsonExt.NpEncoder)``
    '''
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, np.datetime64):   # 这里解决题目上报错
            return str(obj)[:10]
        else:
            return super(NpEncoder, self).default(obj)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
            #return super().default(obj)