from model.group import Group
import time


def test_create_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups = new_groups
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    time.sleep(0.5)





#def random_string(prefix, maxlen):
  #  symbols = string.ascii_letters + string.digits
 #   return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [Group(name="", header="", footer="")] + [
 #   Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
  #  for i in range(5)
#]