from asyncore import dispatcher
from email.message import Message
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler, Filters
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot

updater = Updater(token='5441776897:AAHIsMl17B1avefQ97kYuQWzWzEldfL8_Ak', use_context=True)

bullying_messages = ["МАКС СДЕЛАЙ ДЗ"]

dispatcher1 : Dispatcher = updater.dispatcher

def echo(update: Update, context: CallbackContext):
    if(update.message.from_user.username == 'KXFCODE'):
        update.message.reply_text('МАКС СДЕЛАЙ ДЗ') 

def ping(update: Update, context: CallbackContext):
    update.message.reply_text('pong')


dispatcher1.add_handler(CommandHandler('ping', ping))
dispatcher1.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()