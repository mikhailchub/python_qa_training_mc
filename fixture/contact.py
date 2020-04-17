from model.contact import Contact


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
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        # Fill Contact form
        self.app.set_input_text("firstname", contact.firstname)
        self.app.set_input_text("lastname", contact.lastname)
        self.app.set_input_text("address", contact.address)
        self.app.set_input_text("mobile", contact.mobile)
        self.app.set_input_text("email", contact.email)

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
            element_list = wd.find_elements_by_css_selector("tr[name='entry']")
            for element in element_list:
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                contact_last_name = element.find_element_by_css_selector("td:nth-of-type(2)").text
                contact_first_name = element.find_element_by_css_selector("td:nth-of-type(3)").text
                self.contact_cache.append(Contact(firstname=contact_first_name, lastname=contact_last_name, id=contact_id))
        return list(self.contact_cache)
