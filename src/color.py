#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/2 下午7:36
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : color.py

class ShowOutPut(object):

    def normal(self, message):
        '''显示普通数据'''
        return message

    def blue(self, message):
        '''显示标题'''
        return "\033[1;34m %s \033[0m" % message

    def green(self, message):
        '''显示主机'''
        return "\033[1;32m %s \033[0m" % message

    def purple(self, message):
        '''显示容器名称'''
        return "\033[1;35m %s \033[0m" % message

    def yellow(self, message):
        '''显示时间'''
        return "\033[1;33m %s \033[0m" % message

    def red(self, message):
        '''显示分隔符'''
        return "\033[1;31m %s \033[0m" % message