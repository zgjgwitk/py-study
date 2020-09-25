# -*- coding: utf-8 -*-
import importlib
import os

from conf import gsettings


class Settings(object):
    def __init__(self):
        # 先加载全局配置
        for item in dir(gsettings):
            if item.isupper():
                k = item
                v = getattr(gsettings, k)
                # 给对象设置键值对
                setattr(self, k, v)
        # 加载用户settings
        setting_path = os.environ.get("SETTING")
        settings_module = importlib.import_module(setting_path)
        for s in dir(settings_module):
            if s.isupper():
                k = s
                v = getattr(settings_module, k)
                # 给对象设置键值对
                setattr(self, k, v)


settings = Settings()
