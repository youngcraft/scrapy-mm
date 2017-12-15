# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib2
import pymongo
import platform

class MmspiderPipeline(object):

    def __init__(self):
        if platform.system() == 'Windows':
            self.store_path = os.getcwd() + '\\picture\\'
        else:
            self.store_path = os.getcwd() + '/picture/'

        # self.con = pymongo.MongoClient('127.0.0.1',27017)
        # self.col = self.con.get_database('mm')

        # self.connect = self.col.get_collection('picture')

    def process_item(self, item, spider):
        # print item['name']
        # print item['body']
        # print item['dirname']
        # print self.store_path
        # print item['body'][1:10]
        file_path = self.store_path  + item['name']
        # self.connect.insert_one(item,bypass_document_validation=True)
        req = urllib2.Request(item['_id'])
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')
        req.add_header('Accept', 'image/webp,image/apng,image/*,*/*;q=0.8')
        # print item['_id']
        refer = 'http://www.mm131.com/xinggan/%s.html'  % item['dirname']
        req.add_header('Referer',refer)
        res = urllib2.urlopen(req)

        # print res.read()
        # print res.info()
        # print type(res.read())
        # print file_path

        with open(file_path, 'wb') as f:
            f.write(res.read())

        return item

    def findfileinDir(self,dir,filename):
        pass
