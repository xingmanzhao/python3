#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('',8000, application)
print('Serving HTTP on port 8000')
httpd.serve_forever()
