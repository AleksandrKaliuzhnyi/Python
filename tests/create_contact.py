from model.contact import Contact
import time


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Oleksandr", lastname="Kaliuzhnyi", nickname="emkiss", company="Infopulse", address="Kiev", mobile="0931234567", work="QA",
                      email="test@gmail.com", bday="7", bmonth="December", byear="1994")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    time.sleep(0.5)

#def test_create_empty_contact(app):
#    app.contact.create(Contact("", "", "", "", "", "", "", "", "-", "-", ""))
