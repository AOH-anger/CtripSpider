# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()    #图片地址
    name = scrapy.Field()   #名称
    desc = scrapy.Field()   #描述
    grade = scrapy.Field()  #分数
    price = scrapy.Field()  #价格
    praise = scrapy.Field() #推荐百分比
