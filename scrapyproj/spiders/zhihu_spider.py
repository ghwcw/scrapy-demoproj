# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy

from scrapyproj.items import ZhihuItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu_spider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/xiaowei-zhang-37/following']

    # def start_requests(self):
    #     url = 'https://www.zhihu.com/people/xiaowei-zhang-37/following'
    #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ZhihuItem()
        profile_header = response.xpath('//div[@id="ProfileHeader"]//div[@class="ProfileHeader-content"]')

        items['name'] = profile_header.xpath('.//h1/span[1]/text()').extract()
        items['position'] = profile_header.xpath('.//h1/span[2]/text()').extract()
        items['addr'] = profile_header.xpath('.//div[@class="ProfileHeader-detail"]/div[@class="ProfileHeader-detailItem"][1]/div[@class="ProfileHeader-detailValue"]/span/text()').extract()
        items['industry'] = profile_header.xpath('.//div[@class="ProfileHeader-detail"]/div[@class="ProfileHeader-detailItem"][2]/div[@class="ProfileHeader-detailValue"]/text()').extract()
        items['experience'] = profile_header.xpath('.//div[@class="ProfileHeader-detail"]/div[@class="ProfileHeader-detailItem"][3]/div[@class="ProfileHeader-detailValue"]/div[@class="ProfileHeader-field"]/text()').extract()

        follows = response.xpath('//div[@id="Profile-following"]//div[@class="List-item"]//div[@class="Popover"]//a//text()')

        follow_list = []
        for follow in follows:
            # items['follow'] = follow.extract()
            follow_list.append(follow.extract())

        items['follow'] = follow_list
        print('==>>', items)

        follow_user_url_base = response.xpath('//div[@id="Profile-following"]//div[@class="List-item"]//div[@class="Popover"]//a/@href')

        for url in follow_user_url_base:
            follow_user_url = 'https:'+url.extract()+'/following'
            yield scrapy.Request(url=follow_user_url, callback=self.parse)





