from model.contact import Contact
import time


def test_edit_address(app):
    app.contact.edit(Contact(address="Kharkiv"))
    time.sleep(0.5)

def test_edit_work(app):
    app.contact.edit(Contact(work="AQA"))
