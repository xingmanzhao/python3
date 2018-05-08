#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

import requests

r = requests.get('https://www.douban.com/',params={'q':'python','cat':'1001'})
print('%s\n %s\n %s\n %s\n %s\n' % (r.encoding,r.url,r.content,r.cookies,r.headers))