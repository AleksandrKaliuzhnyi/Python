from model.group import Group
import time

def test_create_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="1st group", header="logo", footer="comment"))
    app.session.logout()
    time.sleep(0.5)

def test_create_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
