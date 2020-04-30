from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(0.5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.open_home_page()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def goto_homepage(self):
        wd = self.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_id("search-az")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def set_input_text(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def destroy(self):
        self.wd.quit()
