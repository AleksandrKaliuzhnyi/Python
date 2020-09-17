from model.contact import Contact
import time
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    return str(random.randint(1, 31))

def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return str(random.choice(months))

def random_year():
    return str(random.randint(1, 9999))

testdata = [Contact(firstname="", lastname="", nickname="")] + [
    Contact(firstname=random_string("firstname", 12), lastname=random_string("lastname", 12), nickname=random_string("nickname", 12), company=random_string("company", 12),
            address=random_string("address", 12), mobile=random_string("mobile", 10), work=random_string("work", 10), email=random_string("email", 10),
            bday=random_day(), bmonth=random_month(), byear=random_year())
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts = new_contacts
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    time.sleep(0.5)
