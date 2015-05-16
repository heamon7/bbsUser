# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import re
import json
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query

from scrapy import log
from datetime import datetime
from scrapy.exceptions import DropItem

from  bbsUser.items import BbsuserItem

class UsererSpider(scrapy.Spider):
    name = "userer"
    allowed_domains = ["bbs.byr.cn"]
    baseUrl = 'http://bbs.byr.cn/user/query/'
    start_urls = (
        'http://bbs.byr.cn/',
    )

    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')

        Users = Object.extend('Users')
        query = Query(Users)
        curTime = datetime.now()
        query.exists('userId')
        query.less_than('createdAt',curTime)
        userCount = query.count()


        print "userCounts: %s" %str(userCount)
        queryLimit = 500
        queryTimes = userCount/queryLimit + 1
        self.urls = []

        for index in range(queryTimes):
            query = Query(Users)
            query.exists('userId')
            query.less_than('createdAt',curTime)
            query.descending('createdAt')
            query.limit(queryLimit)
            query.skip(index*queryLimit)
            query.select('userId')
            userRet = query.find()
            for user in userRet:
                self.urls.append(self.baseUrl + user.get('userId') +".json")
        pass


    def start_requests(self):
       #  print "start_requests ing ......"
       # self.urls = ['http://bbs.byr.cn/user/query/heamon7.json','http://bbs.byr.cn/user/query/wdj1314.json']
        print self.urls
        for url in self.urls:
            yield Request(url,callback = self.parseUser)



    def parseUser(self,response):
        item = BbsuserItem()
	try:
            data = json.loads(response.body.decode('gbk'))
	except:
	    pass
        item['requestId'] = re.split('query/(\w*)\.json',response.url)[1]
	try:
            item['astro'] = data['astro']
	except:
	    item['astro'] = ''
	    item['face_url'] = data['face_url']
            item['face_width'] = data['face_width']
            item['gender'] = data['gender']

            item['home_page'] = data['home_page']
            item['userId'] = data['id']
            item['is_hide'] = data['is_hide']
            item['is_online'] = data['is_online']
            item['last_login_ip'] = data['last_login_ip']

            item['last_login_time'] = data['last_login_time']
            item['level'] =data['level']
            item['life'] = data['life']
            item['msn'] = data['msn']
            item['post_count'] = data['post_count']
            item['qq'] = data['qq']
            item['score'] = data['score']
        item['status'] = data['status']
        item['user_name'] = data['user_name']
        try:
	    item['face_height'] = data['face_height']
	except:
	    item['face_height'] = ''
	try:
	    item['face_url'] = data['face_url']
	except:
	    item['face_url'] =''
	try:
	    
        except:
        try:

        except:
	try:

        except:
	try:

        except:
	try:

        except:
	try:

        except:
	try:

        except:
	try:

        except:
	try:

        except:

        item['face_url'] = data['face_url']
        item['face_width'] = data['face_width']
        item['gender'] = data['gender']

        item['home_page'] = data['home_page']
        item['userId'] = data['id']
        item['is_hide'] = data['is_hide']
        item['is_online'] = data['is_online']
        item['last_login_ip'] = data['last_login_ip']

        item['last_login_time'] = data['last_login_time']
        item['level'] =data['level']
        item['life'] = data['life']
        item['msn'] = data['msn']
        item['post_count'] = data['post_count']
        item['qq'] = data['qq']
        item['score'] = data['score']
        item['status'] = data['status']
        item['user_name'] = data['user_name']

        return item


