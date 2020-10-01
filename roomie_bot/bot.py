#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Hi! I am roomie, a bot with tools to make life easier between roommates.' +
        '\nI can help you tracking your expenses or organizing tasks' +
        '\n\nSend /help for a list of commands'
    )


def pay(update, context):
    pass


def history(update, context):
    pass


def debts(update, context):
    pass


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it bot's token.
    TOKEN = os.environ.get("TOKEN")
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("pay", help))
    dp.add_handler(CommandHandler("history", help))
    dp.add_handler(CommandHandler("debts", help))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until interrupted
    updater.idle()


if __name__ == '__main__':
    main()
