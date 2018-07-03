#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/3 上午12:12
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : check.py

import sys
sys.path.append('../')

from src.common import CommonHanld
from conf import config

def master():
    m = CommonHanld(config.MASTER_HOSTS, config.LOGS_LEVEL)
    m.master_handle()


master()




