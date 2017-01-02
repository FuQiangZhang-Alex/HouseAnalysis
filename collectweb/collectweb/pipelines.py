# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from db_helper import pg_helper as pg

class CollectwebPipeline(object):
    def process_item(self, item, spider):
        # store into pg
        # print('insert: ', item['name'])
        pg.upsert('stage.house_index', item)
        return item
