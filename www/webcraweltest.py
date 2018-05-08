#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

import ssl
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def get_link(url):
    try:
        # method 1 : resolve certificat verify failed
        # context = ssl._create_unverified_context()
        # html = urlopen(url,context=context)

        # method 2 : resolve certificate verify failed
        ssl._create_default_https_context = ssl._create_unverified_context
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,'lxml')
    except AttributeError as e:
        print(e)
    else:
        print(bsObj.prettify())



url = "https://h5.tongyongjifen.cn"
url_signin = 'https://backend.tongyongjifen.cn/loginapi/login.do'
# get_link(url_login)


import requests

def signin(url,params):

    r = requests.post(url_signin, data=params)
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    print(soup.prettify())

params = {'userName':'15910635843','login_pwd':'9c2d4238d304a36169c9df9d02b9993e'}
signin(url_signin,params)
