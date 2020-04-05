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

    def delete_first_contact(self):
        wd = self.app.wd
        # Go to Home page
        self.app.goto_homepage()
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Confirm contact deletion
        wd.switch_to_alert().accept()
        # Return to Home page
        self.app.goto_homepage()

    def update_first_contact(self, contact):
        wd = self.app.wd
        # Go to Home page
        self.app.goto_homepage()
        # Open first contact for editing
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # Fill Contact form
        self.fill_contact_fields(contact)
        # Submit contact update
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # Return to Home page
        self.app.goto_homepage()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        # Fill Contact form
        self.app.set_input_text("firstname", contact.firstname)
        self.app.set_input_text("lastname", contact.lastname)
        self.app.set_input_text("address", contact.address)
        self.app.set_input_text("mobile", contact.mobile)
        self.app.set_input_text("email", contact.email)
