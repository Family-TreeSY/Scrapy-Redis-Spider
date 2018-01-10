# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import datetime


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # item:  (Item 对象) – 被爬取的item
        # (Spider 对象) – 爬取该item的spider
        # 去重，删除重复的数据
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing %s of blogpost from %s' % (data, item['url']))
        if valid:
            homes = [{
                'home_community_name': item['home_community_name'],
                'home_total_price': item['home_total_price'],
                'home_unit_price': item['home_unit_price'],
                'home_reference_down_payment': item['home_reference_down_payment'],
                'home_shape': item['home_shape'],
                'home_decoration': item['home_decoration'],
                'home_tword': item['home_tword'],
                'home_area': item['home_area'],
                'home_build_time': item['home_build_time'],
                'home_time': item['home_time'],
                'home_floor': item['home_floor'],
                'home_header': item['home_header'],
                'home_location': item['home_location'],
                'home_type': item['home_type'],
                # 'home_hape_image': item['home_hape_image'],
                'image_urls': item['image_urls'],
                'data_time': datetime.datetime.now()
            }]

            # 插入数据库集合中
            self.collection.insert(homes)
            log.msg('Item wrote to MongoDB database %s/%s' % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item

