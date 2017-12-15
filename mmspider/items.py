# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    name = scrapy.Field()
    dirname = scrapy.Field()

'''
import random

alpha = [x for x in range(97,122)]
number = [y for y in range(0,9)]

all = number + alpha

flag = ''
for i in range(16):
    t = random.choice(all)
    if t>=97 and t<=122:
        flag += chr(t)
    else:
        flag +=str(t)
print flag


import urllib2
import requests
url = 'http://img1.mm131.me/pic/2194/2.jpg'
print '[*]begin\n'
headers = {
    'user-agent':'I kid you'
}
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener= urllib2.build_opener(httpsHandler,httpsHandler)
# urllib2.install_opener(opener)
req = urllib2.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')
req.add_header('Accept', 'image/webp,image/apng,image/*,*/*;q=0.8')
req.add_header('Referer','http://www.mm131.com/xinggan/2194.html')
res = urllib2.urlopen(req)
# print res.read()
# print res.info()
# print type(res.read())

with open('test.jpg','wb') as f:
    f.write(res.read())

'''

