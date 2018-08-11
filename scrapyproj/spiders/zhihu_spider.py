# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu_spider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/xiaowei-zhang-37/following']

    # def start_requests(self):
    #     url = 'https://www.zhihu.com/people/xiaowei-zhang-37/following'
    #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text.encode())
