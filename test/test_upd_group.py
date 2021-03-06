# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="Test group - upd", header="Test group header - upd",
                                       footer="Test group comment - upd"))
    assert len(old_groups) == app.group.count()


def test_update_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Group - upd")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.update_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

