#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

from bs4 import BeautifulSoup

tml_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(tml_doc,'html.parser')
# print(soup.prettify())
# print(soup.title.name)
# print('%s,%s,%s' % (soup.title.name, soup.title.string,soup.title.parent.name))
# print(soup.p)
# print(soup.p['class'])
# print(soup.p.get('class'))
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link1'))
# for link in soup.find_all('a'):
#     print(link.get('href'))


soup1 = BeautifulSoup('<b class="abc t2">Hey, Want to buy a used parser?</b>','html.parser')
# print(soup1.b)
# print(soup1.b.attrs)
comments = soup1.b.string
# print(comments)
# print(type(comments))

# comments.replace_with('abc')
# print(soup.p.contents)
# print(soup.p.children)

# unicode_b_string = comments.encode('utf-8')
# print(unicode_b_string)
# print(type(unicode_b_string))


# outh = 'I like coding'
# print('%s,%s' % (outh,type(outh)))
# encode_outh = outh.encode('utf-8')
# print('%s,%s' % (encode_outh,type(encode_outh)))

lambdaObj = soup.find_all(lambda tag: len(tag.attrs) == 3)
print(lambdaObj)



