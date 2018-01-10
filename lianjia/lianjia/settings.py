# -*- coding: utf-8 -*-

# Scrapy settings for lianjia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random
import os

BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjia (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
LOG_LEVEL = 'DEBUG'
RANDOMIZE_DOWNLOAD_DELAY = True

# 关闭重定向
REDIRECT_ENABLED = False
# 返回302时,按正常返回对待,可以正常写入cookie
HTTPERROR_ALLOWED_CODES = [302,301]

custom_settings = {
        'RETRY_ENABLED': False

    }
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2995.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.0 Safari/537.36'
]
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Cookie':'lianjia_uuid=82097cd2-8e3d-4b74-99cd-166558cecb1c; UM_distinctid=15ef067be0f8fe-0489011761ffc6-3e63430c-144000-15ef067be1027b; gr_user_id=7cecbf7b-9887-4c2e-943d-28a910608dea; _jzqx=1.1513760669.1513760669.1.jzqsr=link%2Ezhihu%2Ecom|jzqct=/.-; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1511834697,1511952677,1513760668,1514310443; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1514310443; _smt_uid=59d724cc.d7cb818; _jzqa=1.3460179106932847000.1507271884.1513760669.1514310444.11; _jzqc=1; _jzqy=1.1507271884.1514310444.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; _jzqckmp=1; _gid=GA1.2.2047607856.1514310445; aliyungf_tc=AQAAACF6RDCcrwoAvj7uc0C1G/k0NIOi; select_city=310000; cityCode=sh; _ga=GA1.2.307158742.1507271886; __xsptplus696=696.17.1514340983.1514344123.17%234%7C%7C%7C%7C%7C%23%237qsfNSSzVBspSQYZiKl5UVZvo7SRqzWX%23; ubt_load_interval_b=1514344123593; ubta=2299869246.2847147482.1507271888745.1514344122898.1514344124046.133; ubtc=2299869246.2847147482.1514344124048.C1F42B6FDF2DBB2ABEBC71156F946CAC; ubtd=17; gr_session_id_970bc0baee7301fa=6c63c6ff-3491-4c26-9702-c01ebf0f235d',
    # 'Host':'sh.lianjia.com',
    'Referer':'http://sh.lianjia.com/ershoufang/d3',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':random.choice(user_agents)
}
# 图片尺寸
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}

IMAGES_URLS_FIELD = "image_urls"

#获取当前运行脚本的绝对路径（去掉最后一个路径),获取当前爬虫项目的绝对路径
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


# 7天的图片失效期限
IMAGES_EXPIRES = 7

# 图片存储路径
IMAGES_STORE = os.path.join(PROJECT_DIR,'media/lianjia_image')
# IMAGES_STORE = 'D:\\lianjiaimage'
# IMAGES_STORE = 'C:\\Users\\ssaw\\PycharmProjects\\untitled\\lianjia\\image'
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjia.middlewares.LianjiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'lianjia.middlewares.MyCustomDownloaderMiddleware': 543,
    'lianjia.middlewares.RotateUserAgentMiddleware':200,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,
    # 'itjuzi_dis.middlewares.ProxyMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'lianjia.pipelines.LianjiaPipeline': 300,
    # 'lianjia.pipelines.lianjia_image.MyImagesPipeline': 50,
    # 'lianjia.pipelines.lianjia_mongodb.MongoDBPipeline':100,
    # 'lianjia.pipelines.lianjia_json.JsonPipeline':200,
    'scrapy_redis.pipelines.RedisPipeline': 300,
}


MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'ljia'
MONGODB_COLLECTION = 'Shanghai'

#使用Scrapy-Redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#利用Redis的集合实现去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#允许继续爬取
SCHEDULER_PERSIST = True
#设置优先级
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_PARAMS = {'host': 'localhost', 'port': 6379}

# csv设置
FEED_EXPORTERS = {
    'csv': 'lianjia.spiders.csv_item_exporter.MyProjectCsvItemExporter',
}

FEED_EXPORT_ENCODING = 'utf-8'

FIELDS_TO_EXPORT = [
    'home_community_name',
    'home_area',
    'home_unit_price',
    'home_total_price',
    'home_reference_down_payment',
    'home_build_time',
    'home_decoration',
    'home_time',
    'home_floor',
    'home_location',
    'home_type',
    'home_tword',

]





# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
