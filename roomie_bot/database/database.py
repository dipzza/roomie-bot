#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


class Database:
    def __init__(self, dbname="room.sqlite"):
        self._dbname = dbname
        self._conn = sqlite3.connect(dbname)
        self._c = self._conn.cursor()

        self._c.execute('PRAGMA foreign_keys = ON')

    def setup(self):
        self._c.execute('''
                        CREATE TABLE IF NOT EXISTS debts (
                            user_id INT,
                            chat_id INT,
                            debt DOUBLE NOT NULL DEFAULT 0,
                            PRIMARY KEY (user_id, chat_id)
                        );
                        ''')
        self._c.execute('''
                        CREATE TABLE IF NOT EXISTS payments (
                            payment_id INTEGER PRIMARY KEY,
                            user_id INT,
                            chat_id INT,
                            money DOUBLE,
                            description TEXT,
                            FOREIGN KEY (user_id, chat_id)
                            REFERENCES debts(user_id, chat_id)
                            ON DELETE CASCADE
                            ON UPDATE RESTRICT
                        );
                        ''')
        self._conn.commit()

    # Expenses related
    def add_payment(self, user_id: int, chat_id: int, money: float, description: str):
        self._c.execute('''
                        INSERT INTO payments (user_id, chat_id, money, description)
                        VALUES (?, ?, ?, ?);
                        ''', (user_id, chat_id, money, description, ))
        self._conn.commit()

    def get_payments(self, chat_id: int, n: int = 10):
        return self._c.execute('''
                                SELECT payment_id, user_id, money, description FROM payments
                                WHERE chat_id = ?
                                ORDER BY payment_id DESC
                                LIMIT ?
                                ''', (chat_id, n, )).fetchall()

    def add_debt(self, user_id: int, chat_id: int, debt: float):
        self._c.execute('INSERT INTO debts (user_id, chat_id, debt) VALUES (?, ?, ?);', (user_id, chat_id, debt, ))
        self._conn.commit()

    def update_debt(self, user_id: int, chat_id: int, debt: float):
        self._c.execute('''
                        UPDATE debts
                        SET debt = ?
                        WHERE user_id = ? AND chat_id = ?;
                        ''', (debt, user_id, chat_id, ))
        self._conn.commit()

    def get_debt(self, user_id: int, chat_id: int):
        return self._c.execute('SELECT debt FROM debts WHERE user_id = ? AND chat_id = ?',
                               (user_id, chat_id, )).fetchone()

    def get_debts(self, chat_id: int):
        return self._c.execute('SELECT user_id, debt FROM debts WHERE chat_id = ?', (chat_id, )).fetchall()
