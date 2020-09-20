#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from typing import List


class Database:
    def __init__(self, dbname="room.sqlite"):
        self._dbname = dbname
        self._conn = sqlite3.connect(dbname)

    def setup(self):
        pass

    # Expenses related
    def add_payment(self, chat_id: int, money: float, payer: str, debtors: List[str], description: str):
        pass

    def get_payments(self, chat_id: int):
        pass

    def update_debt(self, chat_id: int, money: float, payer: str, debtor: str):
        pass

    def get_debts(self, chat_id: int):
        pass
