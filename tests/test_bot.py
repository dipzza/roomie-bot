#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import mock

import roomie_bot.__main__ as bot


USERNAME = "Usuario"


def test_start():
    update = mock.Mock()

    bot.start(update, None)

    update.message.reply_text.assert_called_once()


def test_register_none():
    update = mock.Mock()
    update.effective_user.username = None

    bot.register(update, None)

    update.message.reply_text.assert_called_once_with(
        'You need an username to /register'
        '\n\nTo set up one go to settings in'
        ' telegram and select "username"'
    )


def test_register():
    update = mock.Mock()
    update.effective_user.username = USERNAME

    with mock.patch('roomie_bot.__main__.Database') as MockedDb:
        bot.register(update, None)

        MockedDb.assert_called_once()
    update.message.reply_text.assert_called_once_with(
        'Successfully registered with username {}'.format(USERNAME)
    )


def test_pay_empty():
    update = mock.Mock()
    context = mock.Mock()
    context.args = ['5']

    bot.pay(update, context)

    update.message.reply_text.assert_called_once_with(
        'Format: /pay money @debtor1 [@debtor2..]'
    )


def test_pay_errors():
    update = mock.Mock()
    context = mock.Mock()
    context.args = ['no_number', '@Dipzza']

    with mock.patch('roomie_bot.__main__.Database') as MockedDb:
        MockedDb.return_value.get_username.return_value = None
        MockedDb.return_value.get_userid.return_value = None
        bot.pay(update, context)
        MockedDb.assert_called_once()

    update.message.reply_text.assert_called_once_with(
        'Error: no_number is not an amount of money\n'
        'Error: You are not registered\n'
        'Error: @Dipzza is not registered\n'
        'Format: /pay money @debtor1 [@debtor2..]'
    )


def test_pay_succesful():
    update = mock.Mock()
    context = mock.Mock()
    context.args = ['5', '@Dipzza']

    with mock.patch('roomie_bot.__main__.Database'):
        with mock.patch('roomie_bot.__main__.expenses') as mocked_expenses:
            bot.pay(update, context)

            mocked_expenses.new_payment.assert_called_once()
    update.message.reply_text.assert_called_once_with(
        'Payment added succesfully'
        '\nCheck new debts with /debts'
    )


def test_history_none():
    update = mock.Mock()

    with mock.patch('roomie_bot.__main__.expenses') as mocked_expenses:
        mocked_expenses.get_payments.return_value = ''
        bot.history(update, None)

        mocked_expenses.get_payments.assert_called_once()
    update.message.reply_text.assert_called_once_with('No history yet')


def test_history():
    update = mock.Mock()

    with mock.patch('roomie_bot.__main__.expenses') as mocked_expenses:
        mocked_expenses.get_payments.return_value = 'history'
        bot.history(update, None)

        mocked_expenses.get_payments.assert_called_once()
    update.message.reply_text.assert_called_once_with('history')


def test_debts_none():
    update = mock.Mock()

    with mock.patch('roomie_bot.__main__.expenses') as mocked_expenses:
        mocked_expenses.get_debts.return_value = ''
        bot.debts(update, None)

        mocked_expenses.get_debts.assert_called_once()
    update.message.reply_text.assert_called_once_with('No debts yet')


def test_debts():
    update = mock.Mock()

    with mock.patch('roomie_bot.__main__.expenses') as mocked_expenses:
        mocked_expenses.get_debts.return_value = 'debt'
        bot.debts(update, None)

        mocked_expenses.get_debts.assert_called_once()
    update.message.reply_text.assert_called_once_with('debt')
