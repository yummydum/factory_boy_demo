import pytest
from factories import AddressFactory
from app import get_address, is_gmails
from conftest import SESSION


@pytest.fixture()
def session():
    yield SESSION
    SESSION.rollback()


@pytest.mark.small
def test_is_gmails(monkeypatch):
    data = [
        AddressFactory.build(),
        AddressFactory.build(email_address='address_2@gmali.com'),
        AddressFactory.build(email_address='address_3@gmailcom')
    ]

    import app
    monkeypatch.setattr(app, 'get_address', lambda x: data)

    result = is_gmails('session mock')
    assert not result


def test_is_gmails_med(session):
    AddressFactory()
    AddressFactory(email_address='address_2@gmali.com')
    AddressFactory(email_address='address_3@gmailcom')
    result = is_gmails(session)
    assert not result