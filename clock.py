from __future__ import unicode_literals

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage, ImageSendMessage

import configparser

from apscheduler.schedulers.blocking import BlockingScheduler

import requests
from bs4 import BeautifulSoup
from fun import database


# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

sched = BlockingScheduler()

@sched.scheduled_job('cron', second='*/10')
def scheduled_job():
    ls = database.show_new()
    if(ls):
        try:
            line_bot_api.push_message(ls[1], ImageSendMessage(original_content_url=ls[2], preview_image_url=ls[2]))
        except:
            print(ls,"失敗")
    else:
        print("目前沒有資料")
sched.start()
