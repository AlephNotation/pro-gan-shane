# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    work_page = scrapy.Field()
    year = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field
