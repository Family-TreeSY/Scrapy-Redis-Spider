> 免责声明：本项目旨在学习Scrapy爬虫框架和MongoDB数据库，不可使用于商业和个人其他意图。若使用不当，均由个人承担。


继上次[Scrapy爬取猫眼电影](https://family-treesy.github.io/2017/12/21/Scrapy%E7%88%AC%E5%8F%96%E7%8C%AB%E7%9C%BC%E7%94%B5%E5%BD%B1/)之后，这几天学习了Scrapy-Redis分布式来提高爬取效率，也算是停留在舒适圈一段时间后往前走了一步！！

**准备工作**
[MongoDB](https://www.mongodb.com/)
[Redis](https://redis.io/)
[Scrapy-Redis](https://github.com/rmax/scrapy-redis)
[Scrapy](https://github.com/scrapy/scrapy)

这次爬取的是[上海自如租房](http://sh.ziroom.com/z/nl/z2.html?qwd=)，相信在魔都生活的小伙伴们如果不是本地人，租房费用占了每月开销很大的一部分，我们来看下租房体验比较好的自如，除了价格贵外 - -！！

#### **实战应用**
创建一个工程
> scrapy startproject ziru

**第一步 编辑item.py**
``` python
import scrapy


class ZiruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ziroom_area = scrapy.Field()
    ziroom_face = scrapy.Field()
    ziroom_floor = scrapy.Field()
    ziroom_label = scrapy.Field()
    # ziroom_location = scrapy.Field()
    ziroom_name = scrapy.Field()
    ziroom_price = scrapy.Field()
    ziroom_type = scrapy.Field()
    ziroom_traffic = scrapy.Field()
    rounding_info = scrapy.Field()
    traffic_info = scrapy.Field()
    ziroom_image = scrapy.Field()
    pass

```

- 首先，引入Scrapy
- 接着，创建一个类，继承自scrapy.item,这个是用来储存要爬下来的数据的存放容器

**第二步 获取网页数据**
在spider文件下创建spider.py
 ![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/vTL5TWP6nxsx3u*xqp2ZyF0SlQj9jH5V*yObgpA6u7Y!/b/dF4BAAAAAAAA&bo=iwWAAgAAAAADBy4!&rf=viewer_4)

``` python
# -*- coding: utf-8 -*-

from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from ziru.items import ZiruItem
from scrapy_redis.spiders import RedisCrawlSpider


class ZiroomSpider(RedisCrawlSpider):
    name = 'ziroom'
    # allowed_domains = ['http://sh.ziroom.com/z/nl/z2.html?qwd=']
    # start_urls = ['http://sh.ziroom.com/z/nl/z2.html?qwd=']
    redis_key = 'ziroomspider:start_urls'
    rules = (
        Rule(LinkExtractor(allow=(r'http://sh.ziroom.com/z/nl/z2.html\?qwd=\&p=\d+'))),
        Rule(LinkExtractor(allow=(r'http:\//sh\.ziroom\.com\/z\/vr\/\d+\.html')), callback='parse_item')
    )

    def parse_item(self, response):
        # print(response.body)
        sel = Selector(response)
        
      ...省略索取元素的代码...

        yield item

```

- 比起Scrapy，又多引入了 from scrapy_redis.spiders import RedisCrawlSpider
- start_urls变为redis_key = 'ziroomspider:start_urls' 作为所有链接存储到 redis
- 爬取rule还是一个链接为翻页，一个为详情页链接

**第三步 编辑管道pipeline.py**

``` python


import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


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
                'ziroom_area': item['ziroom_area'],
                'ziroom_face': item['ziroom_face'],
                'ziroom_floor': item['ziroom_floor'],
                'ziroom_label': item['ziroom_label'],
                # 'ziroom_location': item['ziroom_location'],
                'ziroom_name' :item['ziroom_name'],
                'ziroom_price' : item['ziroom_price'],
                'ziroom_type' : item['ziroom_type'],
                'ziroom_traffic': item['ziroom_traffic'],
                'rounding_info': item['rounding_info'],
                'traffic_info': item['traffic_info'],
                'ziroom_image': item['ziroom_image'],
            }]

            # 插入数据库集合中
            self.collection.insert(homes)
            log.msg('Item wrote to MongoDB database %s/%s' % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item
```

编辑MongoDBpipelines，将获取的数据存入MongoDB数据库中



**第四步 编辑middlewares.py**
在中间件中写入随机选取伪造请求头来防止spider被封掉

``` python

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __int__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        ua = random.choice(self.user_agent_list)
        if ua:
            logging.info(ua)
            request.headers.setdefault('User-Agent', ua)

    # the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
        "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]
```


**第五步 设置setting.py**

这一步要修改配置了

``` python
DOWNLOADER_MIDDLEWARES = {
    # 'ziru.middlewares.MyCustomDownloaderMiddleware': 543,
    'ziru.middlewares.RotateUserAgentMiddleware':200,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,
    # 'itjuzi_dis.middlewares.ProxyMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    'ziru.pipelines.MongoDBPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#使用Scrapy-Redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#利用Redis的集合实现去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#允许继续爬取
SCHEDULER_PERSIST = True
#设置优先级
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_PARAMS = {'host': 'localhost', 'port': '6379'}

```

好了，所有的配置全部部署完了，现在来启动spider来爬取数据吧！！

> scrapy crawl ziroom

![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/Z4440zj2oYT8nndgHw*D8nneUQyvzidoskXf3zHI9.E!/b/dPMAAAAAAAAA&bo=IAPMAQAAAAARB94!&rf=viewer_4)

spider启动，它在等待我们的指令来爬取

打开redis-cli

> lpush ziroomspider:start_urls http://sh.ziroom.com/z/nl/z2.html?qwd=



![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/A6Q6q0FfiRjUjyDCADt4ZOVPO3.BuvLtDyXBZCObz0Y!/b/dD8BAAAAAAAA&bo=KwczAgAAAAADBz8!&rf=viewer_4)

我开了六个spider来爬取，电脑CPU有几个处理器就能开几个，我是8核，最多能开8个，接下来准备学习docker来部署spider
