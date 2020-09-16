from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.select_contact_by_index(index)
        self.delete_contact_button()
        self.app.conf_alert.assertRegexpMatches(self.app.conf_alert.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        self.back_to_home_page()
        self.contact_cache = None

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def edit(self):
        self.edit_contact_by_index(0)

        self.contact_cache = None

    def edit_contact_by_index(self, index, new_contact_data):
        self.edit_contact_button_by_index(index)
        self.fill_contact_form(new_contact_data)
        self.update_contact()
        self.back_to_home_page()
        self.contact_cache = None

    def edit_contact_button(self):
        self.edit_contact_button_by_index(0)

    def edit_contact_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("#maintable > tbody > tr:nth-child(n) > td:nth-child(8)")[index].click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("#maintable > tbody > tr:nth-child(n) > td:nth-child(8)"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname_text = cells[2].text
                lastname_text = cells[1].text
                address_text = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id, all_phones_from_homepage=all_phones, address=address_text, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_button_by_index(index)
        firstname = wd.find_elements_by_name("firstname")[0].get_attribute("value")
        lastname = wd.find_elements_by_name("lastname")[0].get_attribute("value")
        address = wd.find_elements_by_name("address")[0].get_attribute("value")
        email = wd.find_elements_by_name("email")[0].get_attribute("value")
        email2 = wd.find_elements_by_name("email2")[0].get_attribute("value")
        email3 = wd.find_elements_by_name("email3")[0].get_attribute("value")
        home = wd.find_elements_by_name("home")[0].get_attribute("value")
        mobile = wd.find_elements_by_name("mobile")[0].get_attribute("value")
        work = wd.find_elements_by_name("work")[0].get_attribute("value")
        home2 = wd.find_elements_by_name("phone2")[0].get_attribute("value")
        id = wd.find_elements_by_name("id")[0].get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2, email3=email3, home=home, mobile=mobile, work=work, phone2=home2)

    def get_contact_from_view_page(self, index):
        global phone_2, home1, mobile1, work1
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_elements_by_id("content")[0].text
        mobile = re.search("M:(.*)", text)
        if mobile == None:
            mobile1 = None
        elif mobile !=None:
            mobile1 = mobile.group(1)
        work = re.search("W:(.*)", text)
        if work == None:
            work1 = None
        elif work != None:
            work1 = work.group(1)
        home = re.search("H:(.*)", text)
        if home == None:
            home1 = None
        elif home != None:
            home1 = home.group(1)
        phone2 = re.search("P:(.*)", text)
        if phone2 == None:
           phone_2 = None
        elif phone2 != None:
           phone_2 = phone2.group(1)
        return (Contact(mobile=mobile1, work=work1, home=home1, phone2=phone_2))

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name ("td")[6]
        cell.find_element_by_tag_name("a").click()
