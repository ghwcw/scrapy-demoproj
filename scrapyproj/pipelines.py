# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapyproj.settings import MONGO_HOST, MONGO_PORT, MONGO_COLLECTION, MONGO_DB


class ScrapyprojPipeline(object):
    def __init__(self):
        self.host = MONGO_HOST
        self.port = MONGO_PORT
        self.db = MONGO_DB
        self.collection = MONGO_COLLECTION

    def open_spider(self, spiser):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        scrapy_db = self.client[self.db]
        self.novel_coll = scrapy_db[self.collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.novel_coll.insert(data)
        return item

    def close_spider(self, spider):
        self.client.close()
        print('爬虫完毕！数据已存入MongoDB')

