import re
import random


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones(contact_from_edit_page)


def test_phones_on_contact_details_page(app):
    contact_from_details_page = app.contact.get_contact_info_from_details_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_details_page.homephone == contact_from_edit_page.homephone
    assert contact_from_details_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_details_page.workphone == contact_from_edit_page.workphone
    assert contact_from_details_page.secondaryphone == contact_from_edit_page.secondaryphone


def test_contact_info_on_home_page(app):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_phones(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == merge_emails(contact_from_edit_page)


def clean(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clean(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
