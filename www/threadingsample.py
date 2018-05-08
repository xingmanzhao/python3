#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

'training of threading'

__AUTHOR__ = 'xingman zhao'

import time, threading

#新线程的执行代码
def loop():
	print('thread %s is running ...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance += n
	balance -= n

def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(i)
		finally:
			lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


import multiprocessing
def run_loop():
	x = 0
	while True:
		x = x ^ 1

cpu_count = multiprocessing.cpu_count()
print('cpu count : %s' % cpu_count)
for i in range(cpu_count):
	mt = threading.Thread(target=run_loop)
	mt.start()
