#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

'traing of Process'

__AUTHOR = 'xingman zhao'

import os

# print('Process (%s) start ' % os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print('I am child process(%s) and my parenet is %s.' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process(%s).' % (os.getpid(),pid))

from multiprocessing import Process
def run_process(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_process, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

