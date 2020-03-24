# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="TestFirst", lastname="TestLast", address="Somewhere",
                                        email="toster@test.com", mobile="222"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, contact):
        # Open New Contact page
        wd.find_element_by_link_text("add new").click()
        # Fill New Contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Test m name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("toster")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Mr")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("QA Ltd")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("111")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("333")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("444")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("qa@test.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("test@test.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("qatoster.com")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2000")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2002")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Somewhere else")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("555")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("zzz")
        # Submit Contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
