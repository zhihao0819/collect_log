#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/4 上午11:41
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : nodes.py


from color import ShowOutPut
from connect import RemoteOper


class NodesServer(object):

    def __init__(self, host, port, user, passwd, logfile, logslevels):
        self.remote = RemoteOper(host, port, user, passwd, logfile)
        self.host = host
        self.logslevels = logslevels

    def logs_levels(self):
        return [ level.upper()[0] for level in self.logslevels ]

    def get_log_datas(self, server):
        command = 'journalctl -u %s -l --no-pager |sed "1d" ' % server
        return self.remote.command(command)

    def get_log_dates(self, server):
        datas = self.get_log_datas(server)
        dates = []
        for line in datas.split('\n'):
            if len(line.split()) > 0 and line.split()[5][1:] not in dates:
                dates.append(line.split()[5][1:])
        return dates

    def get_log_info(self, server):
        datas = self.get_log_datas(server)
        levels = self.logs_levels()
        infos = []
        for line in datas.split('\n'):
            if len(line) > 0 and ' '.join(line.split()[7:]) not in infos and line.split()[5][0] in levels:
                infos.append(line.split()[5] + ':' ' '.join(line.split()[8:]))
        return infos

    def show_nodes_logs(self, server):
        dates = self.get_log_dates(server)
        infos = self.get_log_info(server)
        mess = ShowOutPut()
        print mess.green("##### %s" % self.host)
        print mess.purple("### %s" % server)
        for date in dates:
            print mess.yellow("# %s" % date)
            for log in set(infos):
                if len(log) > 0 and date in log:
                    print mess.normal("%s : %s" % (infos.count(log), log))

        print mess.red("=========================================\n\n")








