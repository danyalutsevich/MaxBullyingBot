from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("pong")

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    if update.message.from_user.username == "KXFCODE" :
        update.message.reply_text("Макс зроби будь ласка дз")

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5441776897:AAHIsMl17B1avefQ97kYuQWzWzEldfL8_Ak")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("ping", ping))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()