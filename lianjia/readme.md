> 免责声明：本项目旨在学习Scrapy爬虫框架和MongoDB数据库，不可使用于商业和个人其他意图。若使用不当，均由个人承担。


###**简介**
之前用requests + bs4 抓取过宝山区的房源信息，今天我们用scrapy-redis分布式抓取上海17个区所有的房源信息，这个工程比起上一个[scrapy-redis抓取自如网](https://family-treesy.github.io/2017/12/23/scrapy-redis(%E4%B8%80)/)，增加了如下功能：
 - 创建了imagepipeline管道，抓取房型图
 - 输出csv指定了列顺序

这次只总结学习以上两点内容，关于scrapy-redis的实现，有兴趣可以看第一篇[自如](https://family-treesy.github.io/2017/12/23/scrapy-redis(%E4%B8%80)/)

###**所需要的库**
- scrapy
- scrapy-redis
- mongodb
- redis

### **使用图片管道**
新建一个imagepipeline来抓取房型图，这里说下流程

``` python
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item':item,'index':item['image_urls'].index(image_url)})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        # image_paths = os.path.join(PROJECT_DIR,'media/lianjia_image')
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

```

在items.py中添加image_urls、image_paths
``` python
image_urls = scrapy.Field()

image_paths = scrapy.Field()

```

在setting.py中设置如下

``` python
 图片尺寸
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

ITEM_PIPELINES = {
    # 'lianjia.pipelines.LianjiaPipeline': 300,
    'lianjia.pipelines.lianjia_image.MyImagesPipeline': 50,
    ..........

}

```

这里要注意下要在itempipelines中开启图片管道才可以抓取房型图，我在学习的时候遇到了个问题，在setting中设置了请求头，图片地址和HOST不一样，导致出现502 Bad Gateway


### **设置CSV输出列顺序**

1. 我们在spiders文件中新建csv_item_exporter.py


``` python
# -*- coding:utf-8 -*-

from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class MyProjectCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter

        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
            kwargs['fields_to_export'] = fields_to_export

        super(MyProjectCsvItemExporter, self).__init__(*args, **kwargs)

```

2. 设置setting.py

``` python
# csv设置
FEED_EXPORTERS = {
    'csv': 'lianjia.spiders.csv_item_exporter.MyProjectCsvItemExporter',
}

FEED_EXPORT_ENCODING = 'utf-8'

# 按如下名称先后形成列
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


```


![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/enugKHlBEDYoMiH1zUjGpzxHxtUV0jSE1zvPaYJ.37c!/b/dPIAAAAAAAAA&bo=YAWAAgAAAAADB8U!&rf=viewer_4)


![](http://m.qpic.cn/psb?/V10WDaE22S84Sl/M.jMsy7SwPvQbQY8cNrqWhdV*XbS5djeaCOuxWN10uI!/b/dPMAAAAAAAAA&bo=ngSAAgAAAAADBzo!&rf=viewer_4)

### **待解决问题**
- scrapy-redis输出到数据库的数据全部是bytes
- 使用scrapy-redis分布式抓取后，CSV文件出现乱码，txt保存格式直接为ANSI，用Scrapy框架爬取无此问题，我觉得两个问题是有关联的，跪谢各路网友指教！！！！！
