#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/2 下午7:27
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : config.py

# common setting
USER = 'root'
PASSWD = None
PORT = 22
LOG_FILE = '../log/paramiko.log'
LOGS_LEVEL = ('WARN', 'ERROR')

# master setting
MASTER_HOSTS = ('opon0', )

# node setting
NODE_HOSTS = ('opoff0', )
SERVER = 'kubelet'
LOG_NAME = '/tmp/kubelet.log'




