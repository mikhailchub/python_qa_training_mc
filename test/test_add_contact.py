# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="TestFirst", lastname="TestLast", address="Somewhere",
                               email="toster@test.com", mobile="222"))
