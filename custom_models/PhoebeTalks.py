﻿from __future__ import unicode_literals
import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
from custom_models import talk_rand, database, S_code, news,bike
import configparser

import random
import datetime
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))


def save_id(event):
    if '##S' in event.message.text:
        try:
            t = database.save_id(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=t)
            )
            return True
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="儲存失敗")
            )


def save_shopping(event):
    if 'shopee.tw' in event.message.text:
        try:
            L = S_code.s_data(event.message.text)
            #S_code.save_shop(event.source.user_id, event.message.text,L)
            word = "商品名稱:"+L[0]+"\n商品價格"+L[1]+"\n已儲存，降價提醒功能開發中"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=word)
            )
            return True
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="商品儲存失敗，請確認網址")
            )


def newss(event):
    if '新聞' in event.message.text:
        try:
            t = news.new_data()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=t)
            )
            return True
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="幹")
            )


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

def bike_search(event):
    if '查詢' in event.message.text:
        try:
            t = bike.re_show_data(bike.get_data())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=t)
            )
            return True
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="幹")
            )


def bike_count(event):
    if(event.message.text.isdigit()):
        if (int(event.message.text) >= 3001 and int(event.message.text)<=(3329)):
            try:
                t = bike.re_show_bike(bike.get_data(), str(event.message.text))
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=t)
                )
                return True
            except:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="幹")
                )
