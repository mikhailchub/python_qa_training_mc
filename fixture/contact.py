from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # Open New Contact page
        wd.find_element_by_link_text("add new").click()
        # Fill New Contact form
        self.fill_contact_fields(contact)
        # Submit Contact creation
        wd.find_element_by_xpath("//input[@name='submit']").click()
        # Return to Home page
        self.app.goto_homepage()
        # Reset contact cache
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Go to Home page
        self.app.goto_homepage()
        # Select contact by index
        self.select_contact_by_index(index)
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Confirm contact deletion
        wd.switch_to_alert().accept()
        # Delete confirmation page is shown - added as an additional wait
        wd.find_elements_by_css_selector("#content .msgbox")
        # Return to Home page
        self.app.goto_homepage()
        # Reset contact cache
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def update_first_contact(self, contact):
        self.update_contact_by_index(0, contact)

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        # Go to Home page
        self.app.goto_homepage()
        # Open contact for editing by index
        self.open_contact_for_editing_by_index(index)
        # Fill Contact form
        self.fill_contact_fields(contact)
        # Submit contact update
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # Return to Home page
        self.app.goto_homepage()
        # Reset contact cache
        self.contact_cache = None

    def open_contact_for_editing_by_index(self, index):
        wd = self.app.wd
        self.app.goto_homepage()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.app.goto_homepage()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        # Fill Contact form
        self.app.set_input_text("firstname", contact.firstname)
        self.app.set_input_text("lastname", contact.lastname)
        self.app.set_input_text("address", contact.address)
        self.app.set_input_text("home", contact.homephone)
        self.app.set_input_text("mobile", contact.mobilephone)
        self.app.set_input_text("work", contact.workphone)
        self.app.set_input_text("phone2", contact.secondaryphone)
        self.app.set_input_text("email", contact.email)
        self.app.set_input_text("email2", contact.email2)
        self.app.set_input_text("email3", contact.email3)

    def count(self):
        wd = self.app.wd
        self.app.goto_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.goto_homepage()
            self.contact_cache = []
            rows = wd.find_elements_by_name("entry")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                            all_emails_from_homepage=all_emails, all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_for_editing_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        contact = Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                          email=email, email2=email2, email3=email3,
                          homephone=homephone, mobilephone=mobilephone,
                          workphone=workphone, secondaryphone=secondaryphone)
        return contact

    def get_contact_info_from_details_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        contact_details = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", contact_details).group(1)
        mobilephone = re.search("M: (.*)", contact_details).group(1)
        workphone = re.search("W: (.*)", contact_details).group(1)
        secondaryphone = re.search("P: (.*)", contact_details).group(1)
        contact = Contact(homephone=homephone, mobilephone=mobilephone,
                          workphone=workphone, secondaryphone=secondaryphone)
        return contact
