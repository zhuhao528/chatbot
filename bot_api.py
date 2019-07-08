#!/usr/bin/env python
# coding: utf-8
#
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# # from chatterbot.trainers import ListTrainer
# import hug
#
#
# chatbot = ChatBot("deepThought")
# # chatbot.set_trainer(ChatterBotCorpusTrainer)
# trainer = ChatterBotCorpusTrainer(chatbot)
#
# # 使用中文语料库训练它
# trainer.train("chatterbot.corpus.english")  # 语料库
#
# #chatbot = ChatBot("Ron Obvious")
# #trainer = ListTrainer(chatbot)
# #trainer.train("chatterbot.corpus.chinese")
#
#
# @hug.get()
# def get_response(user_input):
#     response = chatbot.get_response(user_input).text
#     return {"response":response}


# 使用微信文档
import requests
import itchat
import time
from threading import Timer
import hug

# 个人
# KEY = 'ac13742c5dec49ef81e12eb2ff10c01b'
# 借用
KEY = 'c0a6905ae52e4c4c86630316cc11a28b'


@hug.get()
def get_response(user_input):
    # 构造发送给图灵机器人服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : user_input,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        # return r.get('text')
        return {"response":r.get('text')}

    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

