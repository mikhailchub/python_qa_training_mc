# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.update_first_contact(Contact(firstname="TestFirst - upd", lastname="TestLast - upd",
                                             address="Somewhere - upd", email="upd@test.com", mobile="222000"))
    assert len(old_contacts) == app.contact.count()


def test_update_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="TestFirst - upd2", lastname="TestLast - upd2")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
