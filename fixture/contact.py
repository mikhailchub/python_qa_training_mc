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
        self.app.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Confirm contact deletion
        wd.switch_to_alert().accept()
        # Return to Home page
        self.app.return_to_homepage()

    def update_first_contact(self, contact):
        wd = self.app.wd
        # Open first contact for editing
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # Fill Contact form
        self.fill_contact_fields(contact)
        # Submit contact update
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # Return to Home page
        self.app.return_to_homepage()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        # Fill Contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
