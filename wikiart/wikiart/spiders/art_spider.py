import scrapy
import pandas as pd
import os
from wikiart.items import WikiartItem

class QuotesSpider(scrapy.Spider):
    name = "artist"
    ARTIST_NAME = "henri-matisse"

    img_dir = '/home/aleph/basin/new-art/wikiart/images/matisse'

    start_urls = [
            'https://www.wikiart.org/en/henri-matisse/all-works/text-list'
        ]

    def parse(self, response):
        for work in response.css(".painting-list-text-row"):
            artwork = WikiartItem()
            work_page = work.css('a::attr(href)').get()
            artwork['title'] = work.css('a::text').get()
            artwork['work_page'] = work_page
            artwork["year"] = work.css("span::text").get()
            #    "title": work.css('a::text').get(),
            ##    "ref": work.css('a::attr(href)').get(),
            #    "year":  work.css("span::text").get()
            #}
            #if res['ref'] is not None:
            #    next_page
            #    yield scrapy.Request()
            request = scrapy.Request("https://www.wikiart.org" + work_page,
                                    callback=self.get_image)
            request.meta['artwork'] = artwork

            yield artwork
            yield request

    def get_image(self, response):
        artwork = response.meta['artwork'] 
        url = response.css("img::attr(src)").extract_first()
        artwork['image_urls'] = [url.split('!')[0]]
        return artwork





class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']