#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/7/2 下午7:44
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : master.py

from color import ShowOutPut

class MasterServer(object):

    def __init__(self, host, logslevels, obj):
        # self.remote = RemoteOper(host, port, user, passwd, logfile)
        self.host = host
        self.logslevels = logslevels
        self.client = obj

    def logs_levels(self):
        return [ level.upper()[0] for level in self.logslevels ]

    def get_container_name(self):
        return self.client.name

    def get_container_dates(self):
        levels = self.logs_levels()
        dates = []
        for log in self.client.logs().split('\n'):
            if len(log) > 0 and log.split()[0][1:] not in dates and log.split()[0][0] in levels:
                dates.append(log.split()[0][1:])
        return dates

    def get_container_logs_data(self):
        levels = self.logs_levels()
        datas = []
        for log in self.client.logs().split('\n'):
            if len(log) > 0 and ' '.join(log.split()[3:]) not in datas and log.split()[0][0] in levels:
                data = log.split()[0] + ' : ' + ' '.join(log.split()[3:])
                datas.append(data)
        return datas

    def show_count_logs(self):
        dates = self.get_container_dates()
        datas = self.get_container_logs_data()
        name = self.get_container_name()
        mess = ShowOutPut()
        print mess.green("##### %s" % self.host)
        print mess.purple("### %s" % name)
        for date in dates:
            print mess.yellow("# %s" % date)
            for log in set(datas):
                if len(log) > 0 and date in log:
                    print mess.normal("%s : %s" % (datas.count(log), log))

        print mess.red("=========================================\n\n")












