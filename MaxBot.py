from asyncore import dispatcher
from email.message import Message
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler, Filters
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot

# from asyncore import dispatcher

# bot = Bot(token='5504760756:AAFiG1aZUlYtxmMGVvVgJuikPG1OVI9-J-M')
updater = Updater(token='5504760756:AAFiG1aZUlYtxmMGVvVgJuikPG1OVI9-J-M', use_context=True)

bullying_messages = ["МАКС СДЕЛАЙ ДЗ"]

dispatcher1 : Dispatcher = updater.dispatcher

def echo(update: Update, context: CallbackContext):
    if(update.message.from_user.username == 'danyalutsevich'):
        update.message.reply_text('МАКС СДЕЛАЙ ДЗ') 

dispatcher1.add_handler(MessageHandler(Filters.text, echo))


updater.start_polling()