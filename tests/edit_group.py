from model.group import Group
import time


def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name="New value"))
    time.sleep(0.5)

def test_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(header="New header"))
