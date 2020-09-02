from model.contact import Contact
import time

def test_create_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("Oleksandr", "Kaliuzhnyi", "emkiss", "Infopulse", "Kiev", "0931234567", "QA",
                            "test@gmail.com", "7", "December", "1994"))
    app.session.logout()
    time.sleep(0.5)

def test_create_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("", "", "", "", "", "", "", "", "-", "-", ""))
    app.session.logout()
