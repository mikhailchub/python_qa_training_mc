# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="TestFirst", lastname="TestLast", address="Somewhere",
                               email="toster@test.com", mobile="222"))
    app.session.logout()
