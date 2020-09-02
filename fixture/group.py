class GroupHelper:

    def __init__(self, app):
        self.app = app

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_list()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation()

    def open_group_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
