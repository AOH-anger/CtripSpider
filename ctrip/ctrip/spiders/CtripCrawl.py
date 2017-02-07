#!/usr/bin/env python
# coding=utf-8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ctrip.items import CtripItem

class CtripSpider(CrawlSpider):
    name ='ctrip'
    allowed_domains = ['ctrip.com']
    # 初始URL
    start_urls = ["http://hotels.ctrip.com/hotel/beijing1/p1"]
    page_lx = LinkExtractor(allow=("p\d+"))

    rules = [Rule(page_lx,callback='parseValue',follow=True)]

    def parseValue(self,response):
        for i in response.xpath("//div[@id='hotel_list']/div/ul"):
            item = CtripItem()
            
            img = i.xpath("./li[1]/div/a/img/@src").extract()[0]
            name = i.xpath("./li[2]/h2/a/@title").extract()[0]
            desc = i.xpath("./li[2]/p[2]/text()").extract()[0]

            # 有部分的条目是没有评分和用户推荐的,所以需要走不同的逻辑
            gradeList = i.xpath("./li[4]/div/a/span[@class='hotel_value']/text()").extract()
            try:
                grade = gradeList[0]
            except:
                grade = i.xpath('./li[4]/div/span/text()').extract()[0]

            price = i.xpath("./li[3]/div/div/a/span/text()").extract()[0]

            praiseList = i.xpath("./li[4]/div/a/span[3]/text()").extract()
            try:
                praise = praiseList[0]
            except:
                praise = 'no praise'

            item['img'] = img.encode('utf-8')
            item['name'] = name.encode('utf-8')
            item['desc'] = desc.encode('utf-8')
            item['grade'] = grade.encode('utf-8')
            item['price'] = price.encode('utf-8')
            item['praise'] = praise.encode('utf-8')

            yield item
