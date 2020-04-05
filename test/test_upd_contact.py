# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    app.contact.update_first_contact(Contact(firstname="TestFirst - upd", lastname="TestLast - upd",
                                             address="Somewhere - upd", email="upd@test.com", mobile="222000"))


def test_update_first_contact_firstname(app):
    app.contact.update_first_contact(Contact(firstname="TestFirst - upd2"))
