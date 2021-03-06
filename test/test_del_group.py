from random import randrange
from model.group import Group


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="Test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
