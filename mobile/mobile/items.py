# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TorrentItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()

class ReviewItem(scrapy.Item):
	url = scrapy.Field()
	restaurant = scrapy.Field()
	review = scrapy.Field()
	rate = scrapy.Field();
	user = scrapy.Field();