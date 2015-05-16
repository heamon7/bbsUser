# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem

class UserPipeline(object):
    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')
        pass
    def process_item(self, item, spider):

        UserInfo = Object.extend('UserInfo')
        UserStatus = Object.extend('UserStatus')
        userInfo = UserInfo()
        userStatus = UserStatus()
        query = Query(UserInfo)
        if item['userId'] != -1:
            query.equal_to('userId',item['userId'])
            try:
                if query.find():
                    pass
                else:
                    # userInfo.set('requestId',item['requestId'])
                    userInfo.set('astro',item['astro'])

                    userInfo.set('face_height',item['face_height'])
                    userInfo.set('face_url',item['face_url'])
                    userInfo.set('face_width',item['face_width'])
                    userInfo.set('gender',item['gender'])
                    userInfo.set('home_page',item['home_page'])
                    userInfo.set('userId',item['userId'])
                    userInfo.set('is_hide',item['is_hide'])
                    userInfo.set('level',item['level'])
                    userInfo.set('msn',item['msn'])
                    userInfo.set('qq',item['qq'])
                    userInfo.set('user_name',item['user_name'])
                    try:
                        userInfo.save()
                    except LeanCloudError,e:
                        print e
            except LeanCloudError,e:
                print e
            userStatus.set('astro',item['astro'])
            userStatus.set('face_height',item['face_height'])
            userStatus.set('face_url',item['face_url'])
            userStatus.set('face_width',item['face_width'])
            userStatus.set('gender',item['gender'])
            userStatus.set('home_page',item['home_page'])
            userStatus.set('userId',item['userId'])

            userStatus.set('is_hide',item['is_hide'])
            userStatus.set('is_online',item['is_online'])
            userStatus.set('last_login_ip',item['last_login_ip'])
            userStatus.set('last_login_time',item['last_login_time'])
            userStatus.set('level',item['level'])
            userStatus.set('life',item['life'])

            userStatus.set('msn',item['msn'])
            userStatus.set('post_count',item['post_count'])

            userStatus.set('qq',item['qq'])
            userStatus.set('score',item['score'])
            userStatus.set('status',item['status'])
            userStatus.set('user_name',item['user_name'])


            try:
                userStatus.save()
            except LeanCloudError,e:
                print e

        if item['debugInfo'] == -1:
            userStatus = UserStatus()
            userStatus.set('requestId',item['requestId'])
            userStatus.set('response',item['response'])
        try:
            userStatus.save()
        except:
            pass
        #return item
        DropItem()

# questionLink
# answerPageNum
#
# floorNumList
# answerPositionList
# userIdList

# userImgLinkList
# userNameList
# userClassList
# userQuestionCountList
# userScoreList

# answerTimeList
# answerIpList
# answerContent
