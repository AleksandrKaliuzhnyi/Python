from model.contact import Contact
import time


def test_edit_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(address="Kharkiv")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    time.sleep(0.5)

#def test_edit_work(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.edit(Contact(work="AQA"))

