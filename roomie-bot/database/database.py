#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


class Database:
    def __init__(self, dbname="room.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        pass

    # Expenses related
    def add_payment(self, id, money, payer, debtors, description):
        pass

    def get_payments(self, id):
        pass

    def update_debt(self, id, money, payer, debtor):
        pass

    def get_debts(self, id, user):
        pass
