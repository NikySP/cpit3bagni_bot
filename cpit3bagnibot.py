import requests
import time
import schedule
from telegram.ext import Updater, CommandHandler
import os
from datetime import datetime

TOKEN = os.getenv("TOKEN")
# GROUPID = os.getenv("")
updater = Updater(TOKEN)
WEBHOOK = os.getenv("WEBHOOK")
MESSAGE = os.getenv("MESSAGE")
PORT = int(os.environ.get('PORT', '8443'))


def bagni(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    bot.send_message(chat_id=chat_id, text=MESSAGE)


while True:
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bagni', bagni))
    updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(WEBHOOK + TOKEN)
    updater.idle()
