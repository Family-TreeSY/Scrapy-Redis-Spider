# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
# import sys

# reload(sys)
# sys.setdefaultencoding('utf8')


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('lianjia.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):

        for i in item['home_community_name']:
            print("~~~~~~~~~~~~~~~~~~~\n")
            print(i)
            print("~~~~~~~~~~~~~~~~~~~~\n")
        line = 'the list:' + '\n'
        home_header = {'home_header': item['home_header']}
        home_total_price = {'home_total_price': item['home_total_price']}
        home_ubit_price = {'home_unit_price': item['home_unit_price']}
        home_reference_down_payment = {'home_reference_down_payment': item['home_reference_down_payment']}
        home_shape = {'home_shape': item['home_shape']}
        home_decoration = {'home_decoration': item['home_decoration']}
        home_tword = {'home_tword': item['home_tword']}
        home_area = {'home_area': item['home_area']}
        home_build_time = {'home_build_time': item['home_build_time']}
        home_build_time = {'home_build_time': item['home_time']}
        home_floor = {'home_floor': item['home_floor']}
        home_community_name = {'home_community_name': item['home_community_name']}
        home_location = {'home_location': item['home_location']}
        home_type = {'home_type': item['home_type']}
        # home_hape_image = {'home_hape_image': item['home_hape_image']}
        home_hape_image = {'home_hape_image': item['image_urls']}

        line = line + json.dumps(home_header, ensure_ascii=False)
        line = line + json.dumps(home_total_price, ensure_ascii=False)
        line = line + json.dumps(home_ubit_price, ensure_ascii=False)
        line = line + json.dumps(home_reference_down_payment, ensure_ascii=False)
        line = line + json.dumps(home_shape, ensure_ascii=False)
        line = line + json.dumps(home_decoration, ensure_ascii=False)
        line = line + json.dumps(home_tword, ensure_ascii=False)
        line = line + json.dumps(home_area, ensure_ascii=False)
        line = line + json.dumps(home_build_time, ensure_ascii=False)
        line = line + json.dumps(home_floor, ensure_ascii=False)
        line = line + json.dumps(home_community_name, ensure_ascii=False)
        line = line + json.dumps(home_location, ensure_ascii=False)
        line = line + json.dumps(home_type, ensure_ascii=False)
        line = line + json.dumps(home_hape_image, ensure_ascii=False) + '\n'
        print('*'*100)

        self.file.write(line)

    def close_spider(self, spider):
        self.file.close()
#
# import json
# import codecs
#
# class JsonPipeline(object):
#
#     def __init__(self):
#         self.file = codecs.open('lianjia.json', 'wb', encoding='utf-8')
#
# def process_item(self, item, spider):
#     line = 'the list:' + '\n'
#     home_header = {'home_header': item['home_header']}
#     home_total_price = {'home_total_price': item['home_total_price']}
#     home_ubit_price = {'home_unit_price': item['home_unit_price']}
#     home_reference_down_payment = {'home_reference_down_payment': item['home_reference_down_payment']}
#     home_shape = {'home_shape': item['home_shape']}
#     home_decoration = {'home_decoration': item['home_decoration']}
#     home_tword = {'home_tword': item['home_tword']}
#     home_area = {'home_area': item['home_area']}
#     home_build_time = {'home_build_time': item['home_time']}
#     home_floor = {'home_floor': item['home_floor']}
#     home_community_name = {'home_community_name': item['home_community_name']}
#     home_location = {'home_location': item['home_location']}
#     home_type = {'home_type': item['home_type']}
#     # home_hape_image = {'home_hape_image': item['home_hape_image']}
#     home_hape_image = {'home_hape_image': item['image_urls']}
#
#     line = line + json.dumps(home_header, ensure_ascii=False)
#     line = line + json.dumps(home_total_price, ensure_ascii=False)
#     line = line + json.dumps(home_ubit_price, ensure_ascii=False)
#     line = line + json.dumps(home_reference_down_payment, ensure_ascii=False)
#     line = line + json.dumps(home_shape, ensure_ascii=False)
#     line = line + json.dumps(home_decoration, ensure_ascii=False)
#     line = line + json.dumps(home_tword, ensure_ascii=False)
#     line = line + json.dumps(home_area, ensure_ascii=False)
#     line = line + json.dumps(home_build_time, ensure_ascii=False)
#     line = line + json.dumps(home_floor, ensure_ascii=False)
#     line = line + json.dumps(home_community_name, ensure_ascii=False)
#     line = line + json.dumps(home_location, ensure_ascii=False)
#     line = line + json.dumps(home_type, ensure_ascii=False)
#     line = line + json.dumps(home_hape_image, ensure_ascii=False) + '\n'
#     print('*'*100)
#
#
#     self.file.write(line)
#
# def spider_closed(self, spider):
#      self.file.close()