from model.contact import Contact
import time

def test_create_contact(app):
    app.contact.create(Contact("Oleksandr", "Kaliuzhnyi", "emkiss", "Infopulse", "Kiev", "0931234567", "QA",
                               "test@gmail.com", "7", "December", "1994"))
    time.sleep(0.5)

def test_create_empty_contact(app):
    app.contact.create(Contact("", "", "", "", "", "", "", "", "-", "-", ""))
