# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    home_header = scrapy.Field()
    home_total_price = scrapy.Field()
    home_unit_price = scrapy.Field()
    home_reference_down_payment = scrapy.Field()
    home_shape = scrapy.Field()
    home_decoration = scrapy.Field()
    home_tword = scrapy.Field()
    home_area = scrapy.Field()
    home_build_time = scrapy.Field()
    home_time = scrapy.Field()
    home_floor = scrapy.Field()
    home_community_name = scrapy.Field()
    home_location = scrapy.Field()
    home_type = scrapy.Field()
    home_hape_image = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
