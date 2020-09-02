import pytest
from model.group import Group
from fixture.application_group import Application_group


@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="1st group", header="logo", footer="comment"))
    app.session.logout()

def test_create_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
