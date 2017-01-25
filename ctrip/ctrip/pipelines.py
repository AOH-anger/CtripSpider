# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CtripPipeline(object):

    def __init__(self):
        self.file = open('ctrip.json','wb')

    def process_item(self, item, spider):
        value = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(value)
        return item

    def close_spider(self,spider):
        self.file.close()
