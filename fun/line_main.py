from __future__ import unicode_literals
import os
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
import configparser
import random
import datetime
from datetime import datetime
from fun import main

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))


def forum_img(event):
    url = event.message.text
    print(url)
    img_url = main.glucose_graph(url)
    print(img_url)
    message = ImageSendMessage(
        original_content_url=img_url, preview_image_url=img_url
    )
    line_bot_api.reply_message(event.reply_token, message)
    return True


def pretty_echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
    return True


def help(event):
    if '##help' in event.message.text:
        try:
            t = "查詢youbike站牌編號:'查詢'\n查詢youbike站牌剩餘車輛:'(站牌編號)'\n隨機觀看新聞:'新聞'\n搜尋蝦皮商城商品價格:'(商品網站)\n開啟提醒通知:##S'"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=t)
            )
            return True
        except:
            return False
