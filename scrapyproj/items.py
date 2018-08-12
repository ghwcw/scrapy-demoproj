# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    section = scrapy.Field()
    author = scrapy.Field()
    words = scrapy.Field()
    update = scrapy.Field()
    status = scrapy.Field()


class ZhihuItem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    addr = scrapy.Field()
    industry = scrapy.Field()       # 行业
    experience = scrapy.Field()     # 经历
    follow = scrapy.Field()         # 关注
