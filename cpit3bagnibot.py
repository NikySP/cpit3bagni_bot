import threading
import requests
import time
import schedule
from telegram.ext import Updater, CommandHandler
import os
from datetime import datetime

TOKEN = os.getenv("TOKEN")
GROUPID = os.getenv("GROUPID")
updater = Updater(TOKEN)
WEBHOOK = os.getenv("WEBHOOK")
MESSAGE = os.getenv("MESSAGE")
PORT = int(os.environ.get('PORT', '8443'))
SCHEDULED_MESSAGE= os.getenv("SCHEDULED_MESSAGE")
PORT = int(os.environ.get('PORT', '8443'))
TRIGGER_TIME = os.getenv("TRIGGER_TIME")
ENABLE_GM = os.getenv("ENABLE_GM")


def bagni(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    bot.send_message(chat_id=chat_id, text=MESSAGE)


def sendGoodMorning():
    bot_chatID = GROUPID
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + SCHEDULED_MESSAGE
    response = requests.get(send_text)
    return response.json()


def loopGoodMorning():
    schedule.every().day.at(TRIGGER_TIME).do(sendGoodMorning)
    while True:
        schedule.run_pending()
        time.sleep(1)

if ENABLE_GM=="y":
    t = threading.Thread(target=loopGoodMorning)
    t.daemon = True
    t.start()

while True:
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bagni', bagni))
    updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(WEBHOOK + TOKEN)
    updater.idle()