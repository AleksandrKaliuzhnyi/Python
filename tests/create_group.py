from model.group import Group
import time

def test_create_group(app):
    app.group.create(Group(name="1st group", header="logo", footer="comment"))
    time.sleep(0.5)

def test_create_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
