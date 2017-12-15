# coding=utf-8
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from mmspider.items import MmspiderItem


class MmSpider(scrapy.Spider):
    name = "mm"
    start_urls = [
        'http://www.mm131.com/xinggan/',
        'http://www.mm131.com/qingchun/',
        'http://www.mm131.com/xiaohua/',
        'http://www.mm131.com/chemo/',
        'http://www.mm131.com/qipao/',
        'http://www.mm131.com/mingxing/'
    ]


    def parse(self, response):
        #
        if response.status == 200:
            for next_url in response.xpath('//dd[@class="page"]/a/@href').extract():
                yield response.follow(next_url,self.parse_next)

    def parse_next(self, response):
        # /html/body/div[5]/dl
        # /html/body/div[5]/dl/dd[2]
        # /html/body/div[5]/dl/dd[1]/a
        if response.status == 200:
            for next_url in response.xpath('//div[@class="main"]/dl/dd/a[@target="_blank"]/@href').extract():
                yield  response.follow(next_url, self.parse_three)

    def parse_three(self, response):
        # http://www.mm131.com/xinggan/3500.html
        if response.status == 200:
            for next_url in response.xpath('//div[@class="content-page"]/a[@class="page-en"]/@href').extract():
                yield  response.follow(next_url,self.parse_four)

    def parse_four(self, response):
        #
        if response.status == 200:
            end_url = response.xpath('//div[@class="content-pic"]/a/img/@src').extract_first()
            yield response.follow(end_url, self.parse_end)

    def parse_end(self, response):
        #l http://img1.mm131.me/pic/2194/2.jpg
        if response.status == 200:
            item = MmspiderItem()
            item['_id'] = response.url
            item['body'] = response.body
            item['name'] = '_'.join([response.url.split('/')[-2], response.url.split('/')[-1]])
            item['dirname'] = response.url.split('/')[-2]
            yield  item


