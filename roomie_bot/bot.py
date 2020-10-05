#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

from database.database import Database
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Initialize database
db = Database()
db.setup()


# Define a few command handlers.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        '''
        Hi! I am roomie, a bot with tools to make life easier between roommates.
        \nI can help you tracking your expenses or organizing tasks
        \nFirst, every user should /register (you should have a username set up)
        \n\nSend /help for a list of commands
        '''
    )


def register(update, context):
    if update.effective_user.username is None:
        update.message.reply_text('You need an username to /register'
                                  '\n\nTo set up one go to settings in'
                                  ' telegram and select "username"')
    else:
        db = Database()
        db.register_user(update.effective_user.id, update.effective_user.username)
        db.close()

        update.message.reply_text('Successfully registered with username ' + update.effective_user.username)


def pay(update, context):
    # Check every user is registered
    # Modify debt
    # Add payment to log
    pass


def history(update, context):
    pass


def debts(update, context):
    db = Database()
    reply = ""

    for debt in db.get_debts(update.effective_chat.id):
        reply += '{}: {}€\n'.format(db.get_username(debt[0]), debt[1])
    db.close()

    update.message.reply_text(reply)


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
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("pay", pay))
    dp.add_handler(CommandHandler("history", history))
    dp.add_handler(CommandHandler("debts", debts))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until interrupted
    updater.idle()


if __name__ == '__main__':
    main()
