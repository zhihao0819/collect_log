#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/2 下午11:08
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : common.py


from master import MasterServer
from color import ShowOutPut
from nodes import NodesServer


class CommonHanld(object):

    def __init__(self, hosts, port, user, passwd, logfile, loglevels):
        self.hosts = hosts
        self.port = port
        self.user = user
        self.passwd = passwd
        self.logfile = logfile
        self.loglevels = loglevels


    def get_containers(self):
        import docker
        self.client = docker.from_env(version='1.24')
        return self.client.containers.list()

    def master_handle(self):
        containers = self.get_containers()
        mess = ShowOutPut()
        print mess.blue("###################### Check k8s-master Container logs ###########################")
        for host in self.hosts:
            for container in containers:
                master = MasterServer(host, self.loglevels, container)
                master.show_count_logs()

    def nodes_handle(self, server):
        mess = ShowOutPut()
        print mess.blue("###################### Check k8s-nodes Container logs ###########################")
        for host in self.hosts:
            node = NodesServer(host, self.port, self.user, self.passwd, self.logfile, self.loglevels)
            node.show_nodes_logs(server)





