from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def update_group(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_list()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_value("group_name", group.name)
        self.change_value("group_header", group.header)
        self.change_value("group_footer", group.footer)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_list(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete(self):
        wd = self.app.wd
        self.open_group_list()
        self.select_group()
        wd.find_element_by_name("delete").click()
        self.open_group_list()
        self.group_cache = None

    def select_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit(self, new_group_data):
        wd = self.app.wd
        self.open_group_list()
        self.select_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        self.update_group()
        self.open_group_list()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_list()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_list()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
