# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.group.update_first_group(Group(name="Test group - upd", header="Test group header - upd",
                                       footer="Test group comment - upd"))


def test_update_first_group_name(app):
    app.group.update_first_group(Group(name="Group - upd"))
