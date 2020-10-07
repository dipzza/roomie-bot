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
    db = Database(":memory:")
    db.setup()

    db.register_user(ID, USERNAME)
    db.add_debt(ID, ID, DEF_DEBT)

    yield db

    db.close()


def test_get_username(sim_db):
    assert sim_db.get_username(ID) == USERNAME


def test_get_username_none(sim_db):
    assert sim_db.get_username(BAD_ID) is None


def test_get_userid(sim_db):
    assert sim_db.get_userid(USERNAME) == ID


def test_get_userid_none(sim_db):
    assert sim_db.get_userid(USERNAME_2) is None


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


def test_get_debts_none(sim_db):
    assert [] == sim_db.get_debts(BAD_ID)


def test_add_debt(sim_db):
    sim_db.add_debt(ID, BAD_ID, MONEY)

    assert MONEY == sim_db.get_debt(ID, BAD_ID)


def test_update_debt(sim_db):
    sim_db.update_debt(ID, ID, MONEY)

    assert MONEY == sim_db.get_debt(ID, ID)


def test_payment(sim_db):
    sim_db.add_payment(ID, ID, MONEY, "")

    assert [(ID, MONEY, "")] == sim_db.get_payments(ID)


def test_get_payment(sim_db):
    sim_db.add_payment(ID, ID, MONEY, "")

    assert (ID, ID, MONEY, "") == sim_db.get_payment(1)
