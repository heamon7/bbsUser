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

        query.equal_to('userId',item['userId'])



        try:
            if query.find():
                pass
            else:
                userInfo.set('requestId',item['requestId'])
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


                query.set('userId',item['userIdList'][index])
                query.set('answerTime',item['answerTimeList'][index])
                query.set('answerIp',item['answerIpList'][index])
                query.set('answerContent',item['answerContentList'][index])
                try:
                    userInfo.save()

                except LeanCloudError,e:
                    print e
        except LeanCloudError,e:
            print e

        UserStatus.set('astro',item['astro'])
        UserStatus.set('face_height',item['face_height'])
        UserStatus.set('face_url',item['face_url'])
        UserStatus.set('face_width',item['face_width'])
        UserStatus.set('gender',item['gender'])
        UserStatus.set('home_page',item['home_page'])
        UserStatus.set('userId',item['userId'])

        UserStatus.set('is_hide',item['is_hide'])
        UserStatus.set('is_online',item['is_online'])
        UserStatus.set('last_login_ip',item['last_login_ip'])
        UserStatus.set('level',item['level'])
        UserStatus.set('life',item['life'])

        UserStatus.set('msn',item['msn'])
        UserStatus.set('post_count',item['post_count'])

        UserStatus.set('qq',item['qq'])
        UserStatus.set('score',item['score'])
        UserStatus.set('status',item['status'])
        UserStatus.set('user_name',item['user_name'])


        try:
            UserStatus.save()
        except LeanCloudError,e:
            print e

        return item
        #DropItem()

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
