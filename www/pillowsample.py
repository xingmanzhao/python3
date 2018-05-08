#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

from PIL import Image, ImageFilter

im = Image.open('1.png')
w,h = im.size
print('Original image size : %sx%s' % (w,h))

# im2 = im.thumbnail((w//2,h//2))
# print('Resize image to : %sx%s' % (w,h))
# im2.save('thumbnail.png','png')

im3 = im.filter(ImageFilter.BLUR)
im3.save('blur.png','png')