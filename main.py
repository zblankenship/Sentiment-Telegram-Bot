import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from parallel import sentiment_check

#boring boiler plate stuff
load_dotenv('key.env')
token = os.getenv('token')
updater = Updater(token = token, use_context = True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#end boring boiler plate stuff

def reply_to_message(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
    reply_to_message_id=update.message.message_id,
    text = sentiment_check(update.message.text))


reply_to_message_handler = MessageHandler(Filters.text & (~Filters.command), reply_to_message)

dispatcher.add_handler(reply_to_message_handler)

updater.start_polling()