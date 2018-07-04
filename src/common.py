#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/2 下午11:08
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : common.py

import docker

from master import MasterServer
from color import ShowOutPut
from nodes import NodesServer

# class Containers(object):
#
#     def __init__(self):
#         self.client = docker.from_env(version='1.24')
#
#     def get_containers(self):
#         return self.client.containers.list()


class CommonHanld(object):

    def __init__(self, hosts, port, user, passwd, logfile, loglevels):
        self.hosts = hosts
        self.port = port
        self.user = user
        self.passwd = passwd
        self.logfile = logfile
        self.loglevels = loglevels
        self.client = docker.from_env(version='1.24')

    def get_containers(self):
        return self.client.containers.list()

    def master_handle(self):
        containers = self.get_containers()
        mess = ShowOutPut()
        print mess.blue("###################### Check k8s-master Container logs ###########################")
        for host in self.hosts:
            for container in containers:
                master = MasterServer(host, self.loglevels, container)
                master.show_count_logs()

    def nodes_handle(self, server, logname):
        mess = ShowOutPut()
        print mess.blue("###################### Check k8s-nodes Container logs ###########################")
        for host in self.hosts:
            node = NodesServer(host, self.port, self.user, self.passwd, self.logfile, self.loglevels)
            node.get_log_file(server, logname)





