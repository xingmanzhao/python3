#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

import re

test = 'a b    c'
obj = re.match(r'\w\s+\w\s+\w', test)
if obj:
    print('OK')
else:
    print(obj)

ob1 = re.split(r'[\s\,\;]+','a,b c  d;e')
print(ob1)

print(re.match(r'^(\d+)(0*)$','102300').groups())
print(re.match(r'^(\d+?)(0*)$','102300').groups())