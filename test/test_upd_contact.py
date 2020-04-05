# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(firstname="TestFirst - upd", lastname="TestLast - upd",
                                             address="Somewhere - upd", email="upd@test.com", mobile="222000"))
    app.session.logout()


def test_update_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(firstname="TestFirst - upd2"))
    app.session.logout()
