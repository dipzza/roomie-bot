#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from roomie_bot.database.database import Database
import roomie_bot.expenses.expenses as expenses

ID = 1
ID_2 = 20
DEF_DEBT = 0.0
USERNAME = "Usuario"
USERNAME_2 = "Usuario_2"
MONEY = 5.0

TEST_DB = "test.sqlite"


@pytest.fixture
def sim_db():
    db = Database(TEST_DB)
    db.setup()

    db.register_user(ID, USERNAME)
    db.register_user(ID_2, USERNAME_2)
    db.add_debt(ID, ID, DEF_DEBT)

    db._conn.commit()

    yield db

    db.close()


def test_is_number():
    assert expenses.is_number("2")
    assert expenses.is_number("1.01")
    assert not expenses.is_number("No")


def test_get_debts(sim_db):
    assert expenses.get_debts(ID, TEST_DB) == '{}: {}€\n'.format(USERNAME, DEF_DEBT)

def test_get_payments(sim_db):
    sim_db.add_payment(ID, ID, MONEY, "")
    
    assert expenses.get_payments(ID, TEST_DB) == '{} payed {} for {}\n'.format(USERNAME, MONEY, '')
    
    sim_db._c.execute('DELETE FROM payments WHERE payment_id = 1;')
    sim_db._conn.commit()

def test_new_payment_branch_1(sim_db):
    expenses.new_payment(ID, ID, MONEY, [ID_2], [USERNAME_2], 2, TEST_DB)

    assert sim_db.get_debt(ID, ID) == MONEY
    assert sim_db.get_debt(ID_2, ID) == -MONEY
    assert sim_db.get_payments(ID, 1) == [(1, ID, MONEY, USERNAME_2)]

    sim_db.update_debt(ID, ID, DEF_DEBT)
    sim_db._c.execute('DELETE FROM debts WHERE user_id = ?;', (ID_2, ))
    sim_db._c.execute('DELETE FROM payments WHERE user_id = ?;', (ID, ))
    sim_db._conn.commit()


def test_new_payment_branch_2(sim_db):
    expenses.new_payment(ID_2, ID, MONEY, [ID], [USERNAME], 2, TEST_DB)

    assert sim_db.get_debt(ID, ID) == -MONEY
    assert sim_db.get_debt(ID_2, ID) == MONEY
    assert sim_db.get_payments(ID, 1) == [(1, ID_2, MONEY, USERNAME)]

    sim_db.update_debt(ID, ID, DEF_DEBT)
    sim_db._c.execute('DELETE FROM debts WHERE user_id = ?;', (ID_2, ))
    sim_db._c.execute('DELETE FROM payments WHERE user_id = ?;', (ID_2, ))
    sim_db._conn.commit()
