import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("Oleksandr", "Kaliuzhnyi", "emkiss", "Infopulse", "Kiev", "0931234567", "QA",
                            "test@gmail.com", "7", "December", "1994"))
    app.session.logout()

def test_create_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("", "", "", "", "", "", "", "", "-", "-", ""))
    app.session.logout()
