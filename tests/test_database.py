#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from roomie_bot.database.database import Database

ID = 1
BAD_ID = 10
USERNAME = "Usuario"
USERNAME_2 = "Usuario2"
MONEY = 5.0
DEF_DEBT = 0.0


@pytest.fixture
def sim_db():
    db = Database("test.sqlite")
    db.setup()

    db.register_user(ID, USERNAME)
    db._c.execute('INSERT OR REPLACE INTO debts (user_id, chat_id) VALUES (?, ?);', (ID, ID, ))

    db._conn.commit()

    yield db

    db.close()


def test_get_username(sim_db):
    assert sim_db.get_username(ID) == USERNAME


def test_get_userid(sim_db):
    assert sim_db.get_userid(USERNAME) == ID


def test_register_user(sim_db):
    sim_db.register_user(BAD_ID, USERNAME_2)

    assert sim_db.get_username(BAD_ID) == USERNAME_2

    sim_db.remove_user(BAD_ID)

    assert sim_db.get_username(BAD_ID) is None


def test_get_debt(sim_db):
    assert DEF_DEBT == sim_db.get_debt(ID, ID)


def test_get_debt_none(sim_db):
    assert sim_db.get_debt(BAD_ID, BAD_ID) is None


def test_get_debts(sim_db):
    assert [(ID, DEF_DEBT)] == sim_db.get_debts(ID)


def test_add_debt(sim_db):
    sim_db.add_debt(ID, BAD_ID, MONEY)

    assert MONEY == sim_db.get_debt(ID, BAD_ID)

    sim_db._c.execute('DELETE FROM debts WHERE chat_id = ?;', (BAD_ID, ))
    sim_db._conn.commit()


def test_update_debt(sim_db):
    sim_db.update_debt(ID, ID, MONEY)

    assert MONEY == sim_db.get_debt(ID, ID)

    sim_db.update_debt(ID, ID, DEF_DEBT)


def test_payment(sim_db):
    sim_db.add_payment(ID, ID, MONEY, "")

    assert [(1, ID, MONEY, "")] == sim_db.get_payments(ID, 1)

    sim_db._c.execute('DELETE FROM payments WHERE payment_id = 1;')
    sim_db._conn.commit()
