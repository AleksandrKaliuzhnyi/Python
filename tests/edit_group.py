from model.group import Group
import time

def test_edit_name(app):
    app.group.edit(Group(name="New value"))
    time.sleep(0.5)

def test_edit_header(app):
    app.group.edit(Group(header="New header"))
