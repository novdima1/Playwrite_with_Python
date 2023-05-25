import pytest


@pytest.mark.relationship
def test_add_relationship(login):
    page = login.\
        click_adviser_workplace()


@pytest.mark.relationship
def test_edit_relationship():
    pass


@pytest.mark.relationship
def test_delete_relationship():
    pass


def test_add_template_category(login):
    page = login
    page.add_template_category()


def test_add_dd_templates_and_promote(login):
    page = login
    for i in range(3100, 3300):
        page.add_dd_template_and_promote(f"test_name_{i}", "111")


def test_promote_templates(login):
    page = login
    for i in range(3100, 3300):
        page.promote_template(f"test_name_{i}")
