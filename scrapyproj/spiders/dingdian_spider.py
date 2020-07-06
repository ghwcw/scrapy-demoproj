#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2018-07-11
    Project : scrapyproj
   FileName : dingdian_spider.py
Description : 爬虫文件
-------------------------------------------------------------
"""
import scrapy
from scrapyproj.items import ScrapyprojItem


class DingDianSpider(scrapy.Spider):
    name = 'dingdian_spider'
    # 允许的域名，非此域名则不抓取
    allowed_domains = ['23us.com']         # 【顶点小说】
    leftpart_url = 'http://www.23us.com/class/'
    rightpart_url = '.html'

    custom_settings = {
        'ITEM_PIPELINES': {'scrapyproj.pipelines.ScrapyprojPipeline': 300, }
    }

    # 可以直接全使用start_urls装入全部请求，不过并不太美观。可以重写start_requests方法
    # 按小说类别分别爬取
    def start_requests(self):
        for i in range(1, 11):
            urls = self.leftpart_url + str(i) + '_1' + self.rightpart_url
            yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        dd_items = ScrapyprojItem()
        novels = response.xpath('//div[@class="bdsub"]//dl[@id="content"]//dd//table//tr[position()>1]')
        count = 0
        for item in novels:
            count += 1
            dd_items['name'] = item.xpath('.//td/a[2]/text()').extract_first()
            dd_items['section'] = item.xpath('./td[2]//text()').extract_first()
            dd_items['author'] = item.xpath('./td[3]//text()').extract_first()
            dd_items['words'] = item.xpath('./td[4]//text()').extract_first()
            dd_items['update'] = item.xpath('./td[5]//text()').extract_first()
            dd_items['status'] = item.xpath('./td[6]//text()').extract_first()
            yield dd_items

        # 爬取下一页，数据量大
        # next_page_sl = response.xpath('//div[@id="pagelink"]/a[@class="next"]/@href').extract_first()
        # if next_page_sl:
        #     yield scrapy.Request(url=next_page_sl, callback=self.parse)
