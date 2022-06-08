#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 17523431, #get it from https://my.telegram.org/auth
    api_hash="1ffee6baec94c9e4c2e4ff87d6abf788", #get it from https://my.telegram.org/auth
    bot_token="5577137798:AAFzY5j-kdjb6C789sElM7NRB3XyTH_VNqg", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
