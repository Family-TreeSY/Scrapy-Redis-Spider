# -*- coding: utf-8 -*-

from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from lianjia.items import LianjiaItem
from scrapy_redis.spiders import RedisCrawlSpider


class LjiaSpider(RedisCrawlSpider):
    name = 'lianjia'
    # allowed_domains = ['http://sh.lianjia.com/ershoufang/d1']
    # start_urls = ['http://sh.lianjia.com/ershoufang/d1']
    # start_urls = [
    #     'http://sh.lianjia.com/ershoufang/pudong/d1',
    #     'http://sh.lianjia.com/ershoufang/minhang/d1',
    #     'http://sh.lianjia.com/ershoufang/baoshan/d1',
    #     'http://sh.lianjia.com/ershoufang/xuhui/d1',
    #     'http://sh.lianjia.com/ershoufang/putuo/d1',
    #     'http://sh.lianjia.com/ershoufang/yangpu/d1',
    #     'http://sh.lianjia.com/ershoufang/changning/d1',
    #     'http://sh.lianjia.com/ershoufang/songjiang/d1',
    #     'http://sh.lianjia.com/ershoufang/jiading/d1',
    #     'http://sh.lianjia.com/ershoufang/huangpu/d1',
    #     'http://sh.lianjia.com/ershoufang/jingan/d1',
    #     'http://sh.lianjia.com/ershoufang/zhabei/d1',
    #     'http://sh.lianjia.com/ershoufang/hongkou/d1',
    #     'http://sh.lianjia.com/ershoufang/qingpu/d1',
    #     'http://sh.lianjia.com/ershoufang/fengxian/d1',
    #     'http://sh.lianjia.com/ershoufang/jinshan/d1',
    #     'http://sh.lianjia.com/ershoufang/chongming/d1',
    #
    # ]

    redis_key = 'lianjiaspider:start_urls'

    rules = (
        # Rule(LinkExtractor(allow=(r'http://sh\.lianjia\.com/ershoufang/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/pudong/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/minhang/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/baoshan/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/xuhui/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/putuo/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/yangpu/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/changning/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/songjiang/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/jiading/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/huangpu/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/jingan/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/zhabei/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/hongkou/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/qingpu/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/fengxian/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/jinshan/d\d+'))),
        Rule(LinkExtractor(allow=(r'http://sh.lianjia.com/ershoufang/chongming/d\d+'))),

        Rule(LinkExtractor(allow=(r'http://sh\.lianjia\.com/ershoufang/sh\d+\.html')), callback='parse_item')
    )


    def parse_item(self, response):
        sel = Selector(response)
        home_header = sel.xpath('/html/body/section/header/div/div[2]/h1/text()').extract()
        home_total_price = sel.xpath('/html/body/section/div[2]/aside/div[1]/div[1]/span[1]/text()').extract()
        home_unit_price = sel.xpath('/html/body/section/div[2]/aside/div[1]/div[2]/p/span/text()').extract()
        # 参考首付预算含税
        home_reference_down_payment = sel.xpath('//*[@id="firstPayContainer"]/a/span/text()').extract()
        # 户型
        home_shape = sel.xpath('/html/body/section/div[2]/aside/ul[1]/li[1]/p[1]/text()').extract()
        # 装修程度
        home_decoration = sel.xpath('/html/body/section/div[2]/aside/ul[1]/li[1]/p[2]/text()').extract()
        # 房屋朝向
        home_tword = sel.xpath('/html/body/section/div[2]/aside/ul[1]/li[2]/div/p[1]/text()').extract()
        home_area = sel.xpath('/html/body/section/div[2]/aside/ul[1]/li[3]/p[1]/text()').extract()
        home_build_time = sel.xpath('/html/body/section/div[2]/aside/ul[1]/li[3]/p[2]/text()').extract()
        # 是否满五年
        home_time = sel.xpath('//*[@id="js-baseinfo-header"]/div[1]/div[2]/div[2]/ul/li[2]/span[2]/text()').extract()
        home_floor = sel.xpath('//*[@id="js-baseinfo-header"]/div[1]/div[1]/div[3]/ul/li[1]/span[2]/text()').extract()
        home_community_name = sel.xpath('/html/body/section/div[2]/aside/ul[2]/li[4]/span[2]/span/a[1]/text()').extract()
        home_location = sel.xpath('/html/body/section/div[2]/aside/ul[2]/li[5]/span[2]/text()').extract()
        # 房屋类型
        home_type = sel.xpath('//*[@id="js-estate-intro"]/div[1]/div/div[2]/ul/li[3]/span[2]/text()').extract()
        # 户型图
        # home_hape_image = sel.xpath('//div[@class="main-pic"]/img/@src').extract()
        # 房源照片
        # image_urls = sel.xpath('//div[@class="list-item"]/img/@src').extract()
        image_urls = sel.xpath('//div[@class="main-pic"]/img/@src').extract()

        # print(home_header)
        # print(home_total_price)
        # print(home_unit_price)
        # print(home_reference_down_payment)
        # print(home_shape)
        # print(home_decoration)
        # print(home_tword)
        # print(home_area)
        # print(home_build_time)
        # print(home_time)
        # print(home_floor)
        # print(home_community_name)
        # print(home_location)
        # print(home_type)
        # print(home_hape_image)
        # print(image_urls)

        item = LianjiaItem()

        item['home_community_name'] = home_community_name
        item['home_total_price'] = home_total_price
        item['home_unit_price'] = home_unit_price
        item['home_reference_down_payment'] = home_reference_down_payment
        item['home_shape'] = home_shape
        item['home_decoration'] = home_decoration
        item['home_tword'] = home_tword
        item['home_area'] = home_area
        item['home_build_time'] = home_build_time
        item['home_time'] = home_time
        item['home_floor'] = home_floor
        item['home_header'] = home_header
        item['home_location'] = home_location
        item['home_type'] = home_type
        # item['home_hape_image'] = home_hape_image
        item['image_urls'] = image_urls

        yield item
