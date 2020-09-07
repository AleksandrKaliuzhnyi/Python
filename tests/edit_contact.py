from model.contact import Contact
import time


def test_edit_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit(Contact(address="Kharkiv"))
    time.sleep(0.5)

def test_edit_work(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit(Contact(work="AQA"))
