# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbsuserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    debugInfo = scrapy.Field()
    response = scrapy.Field()
    requestId = scrapy.Field()
    astro = scrapy.Field()
    face_height = scrapy.Field()
    face_url = scrapy.Field()
    face_width = scrapy.Field()
    gender = scrapy.Field()
    home_page = scrapy.Field()
    userId = scrapy.Field()
    is_hide = scrapy.Field()
    is_online = scrapy.Field()
    last_login_ip = scrapy.Field()
    last_login_time = scrapy.Field()
    level = scrapy.Field()
    life = scrapy.Field()
    msn = scrapy.Field()
    post_count = scrapy.Field()
    qq = scrapy.Field()
    score = scrapy.Field()
    status = scrapy.Field()
    user_name = scrapy.Field()
