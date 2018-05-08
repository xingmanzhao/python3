#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None

    try:
        bsObj = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        # print(bsObj.prettify())
        # bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.html.body.h1.string
    except AttributeError as e:
        return None

    return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not been found')
else:
    print(title)

