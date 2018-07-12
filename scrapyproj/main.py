#!/usr/bin/env python
# coding:utf-8
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2018-07-11
    Project : scrapyproj
   FileName : main.py
Description : 
-------------------------------------------------------------
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl dingdian'.split())
