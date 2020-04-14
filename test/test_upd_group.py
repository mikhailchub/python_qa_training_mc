# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="Test group - upd", header="Test group header - upd",
                                       footer="Test group comment - upd"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Group - upd")
    group.id = old_groups[0].id
    app.group.update_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

