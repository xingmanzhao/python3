#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

import psutil

print('%s,%s' % (psutil.cpu_count(),psutil.cpu_count(logical=False)))
print('%s,%s' % (psutil.cpu_times(), psutil.cpu_percent()))

# for i in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())
print(psutil.disk_usage('/Users/xingman/'))
print(psutil.disk_io_counters())

print(psutil.test())