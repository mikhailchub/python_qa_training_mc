# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.update_first_group(Group(name="Test group - upd", header="Test group header - upd",
                                       footer="Test group comment - upd"))


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.update_first_group(Group(name="Group - upd"))
