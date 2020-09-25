# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

# 设置一个全局的键值对
os.environ.setdefault('SETTING', 'lib.settings')
from conf import settings
print(BASE_DIR)
print(settings.NAME)
