class GroupHelper:

    def __init__(self, app):
        self.app = app

    def goto_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Navigate to Groups page
        self.goto_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        self.fill_group_fields(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        # Return to Groups page
        self.goto_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.goto_groups_page()
        self.select_first_group()
        # Submit deletion
        wd.find_element_by_name("delete").click()
        # Return to Groups page
        self.goto_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        # Select first group
        wd.find_element_by_name("selected[]").click()

    def update_first_group(self, group):
        wd = self.app.wd
        self.goto_groups_page()
        self.select_first_group()
        # Open group for editing
        wd.find_element_by_name("edit").click()
        # Fill group form
        self.fill_group_fields(group)
        # Submit group creation
        wd.find_element_by_name("update").click()
        # Return to Groups page
        self.goto_groups_page()

    def fill_group_fields(self, group):
        # Fill group form
        self.app.set_input_text("group_name", group.name)
        self.app.set_input_text("group_header", group.header)
        self.app.set_input_text("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        self.goto_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
