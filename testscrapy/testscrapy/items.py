# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanFilmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_name=scrapy.Field()
    score = scrapy.Field()
    introduction = scrapy.Field()

    pass
