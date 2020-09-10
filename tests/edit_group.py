from model.group import Group
import time


def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="test")
    group.id = old_groups[0].id
    app.group.edit(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    time.sleep(0.5)

#def test_edit_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    group = Group(header="New header")
#    app.group.edit(group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
