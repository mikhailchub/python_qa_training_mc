# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".com"


def random_phone(prefix, maxlen):
    symbols = string.digits*100 + string.ascii_letters + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("First ", 10), lastname=random_string("Last ", 10),
            address=random_string("Address ", 30),
            email=random_email("email", 5), email2=random_email("email", 5), email3=random_email("email", 5),
            homephone=random_phone("+", 15), mobilephone=random_phone("+", 15), workphone=random_phone("+", 15),
            secondaryphone=random_phone("+", 15))
    for firstname in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
