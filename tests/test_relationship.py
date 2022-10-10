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
