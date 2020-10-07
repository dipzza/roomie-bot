#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pytest

from roomie_bot.api_rest import server
from roomie_bot.database.database import Database

ID = 1
BAD_ID = 10
DEF_DEBT = 0.0
USERNAME = "Usuario"
MONEY = 5.0


@pytest.fixture
def client():
    server.app.config["TESTING"] = True
    server.app.config["DATABASE"] = "test.sqlite"

    with server.app.test_client() as client:
        yield client


@pytest.fixture
def sim_db():
    db = Database("test.sqlite")
    db.setup()

    yield db

    db.clean()
    db.close()


def test_get_user(client, sim_db):
    sim_db.register_user(ID, USERNAME)

    request = client.get('/api/users/{}'.format(ID))
    user_id = json.loads(request.data)["user_id"]
    username = json.loads(request.data)["username"]

    assert user_id == ID
    assert username == USERNAME


def test_get_user_none(client, sim_db):
    request = client.get('/api/users/{}'.format(BAD_ID))

    assert len(json.loads(request.data)) == 0


def test_get_debt(client, sim_db):
    sim_db.register_user(ID, USERNAME)
    sim_db.add_debt(ID, ID, DEF_DEBT)

    request = client.get('/api/debts/{}/{}'.format(ID, ID))
    user_id = json.loads(request.data)["user_id"]
    chat_id = json.loads(request.data)["chat_id"]
    debt = json.loads(request.data)["debt"]

    assert user_id == ID
    assert chat_id == ID
    assert debt == DEF_DEBT


def test_get_debt_none(client, sim_db):
    request = client.get('/api/debts/{}/{}'.format(BAD_ID, BAD_ID))

    assert len(json.loads(request.data)) == 0


def test_get_payment(client, sim_db):
    sim_db.register_user(ID, USERNAME)
    sim_db.add_debt(ID, ID, DEF_DEBT)
    sim_db.add_payment(ID, ID, MONEY, "")

    request = client.get('/api/payments/1')
    user_id = json.loads(request.data)["user_id"]
    chat_id = json.loads(request.data)["chat_id"]
    money = json.loads(request.data)["money"]
    desc = json.loads(request.data)["desc"]

    assert user_id == ID
    assert chat_id == ID
    assert money == MONEY
    assert desc == ""


def test_get_payment_none(client, sim_db):
    request = client.get('/api/payments/{}'.format(BAD_ID))

    assert len(json.loads(request.data)) == 0
