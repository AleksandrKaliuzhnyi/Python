from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.accept_next_alert = True

    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def back_to_home_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("home")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        self.add_new_contact_button()
        self.fill_contact_form(contact)
        self.submit_update_form()
        self.back_to_home_page()

    def fill_contact_form(self, contact):
        self.change_value("firstname", contact.firstname)
        self.change_value("lastname", contact.lastname)
        self.change_value("nickname", contact.nickname)
        self.change_value("company", contact.company)
        self.change_value("address", contact.address)
        self.change_value("mobile", contact.mobile)
        self.change_value("work", contact.work)
        self.change_value("email", contact.email)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_value("byear", contact.byear)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def add_new_contact_button(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def submit_update_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete(self):
        self.select_contact()
        self.delete_contact_button()
        self.app.conf_alert.assertRegexpMatches(self.app.conf_alert.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        self.back_to_home_page()

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_contact_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def edit(self, new_contact_data):
        self.edit_contact_button()
        self.fill_contact_form(new_contact_data)
        self.update_contact()
        self.back_to_home_page()

    def edit_contact_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_css_selector("#maintable > tbody > tr:nth-child(n) > td:nth-child(1)"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, lastname=text, id=id))
        return contacts
