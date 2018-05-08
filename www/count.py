#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


'training of closure'

__author__ = ' xingmanzhao'

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = count()
f1()
f2()
f3()