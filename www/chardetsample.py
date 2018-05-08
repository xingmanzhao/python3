#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

import chardet

print(chardet.detect(b'Hello world!'))

data = '随风潜入夜，润物细无声'.encode('GBK')
print(chardet.detect(data))