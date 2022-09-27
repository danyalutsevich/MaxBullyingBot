from __future__ import print_function
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("pong")

def echo(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.username == "KXFCODE" :
        update.message.reply_text("Макс зроби будь ласка дз")
    elif update.message.from_user.username == "obn1601" :
        update.message.reply_text("Омар зроби будь ласка дз")
    print(f"{update.message.from_user.id} {update.message.from_user.username}")

def main() -> None:
    updater = Updater("5441776897:AAHIsMl17B1avefQ97kYuQWzWzEldfL8_Ak")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("ping", ping))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()