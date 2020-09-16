from random import randrange
import re


def test_data_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_homepage.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_homepage.address == clear(contact_from_edit_page.address)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)

def test_data_on_contact_view_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_view__page = app.contact.get_contact_from_view_page(index)
    a = merge_phones_like_on_homepage(contact_from_view__page)
    assert contact_from_homepage.all_phones_from_homepage == a

def clear(s):
     return re.sub('[() -]', "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                            filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
