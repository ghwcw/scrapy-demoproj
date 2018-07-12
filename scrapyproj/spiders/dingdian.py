#!/usr/bin/env python
# coding:utf-8
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2018-07-11
    Project : scrapyproj
   FileName : dingdian.py
Description : 
-------------------------------------------------------------
"""
import scrapy
from bs4 import BeautifulSoup

from scrapyproj.items import ScrapyprojItem


class DingDianSpider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['x23us.com']
    leftpart_url = 'http://www.x23us.com/class/'
    rightpart_url = '.html'

    # 可以直接全使用start_urls装入全部请求，不过并不太美观。可以重写start_requests方法
    def start_requests(self):
        for i in range(1,11):
            urls = self.leftpart_url+str(i)+'_1'+self.rightpart_url
            yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
       pass
