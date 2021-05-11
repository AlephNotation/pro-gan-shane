# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

class WikiartPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item.get('image_url', []):
            request = scrapy.Request(image_url)
            request.meta['title'] = item['title']
            yield request

    def file_path(self, request, response=None, info=None):
        return 'full/%s.jpg' % request.meta.get('title')