import pytest
from factories import AddressFactory
from app import get_addresses, is_hogemails
from conftest import SESSION


@pytest.fixture()
def session():
    yield SESSION
    SESSION.rollback()


@pytest.mark.small
def test_is_hogemails(monkeypatch):
    data = [
        AddressFactory.build(),
        AddressFactory.build(email_address='address_2@hogemali.com'),
        AddressFactory.build(email_address='address_3@hogemailcom')
    ]

    import app
    monkeypatch.setattr(app, 'get_addresses', lambda x: data)

    result = is_hogemails('session mock')
    assert not result


def test_is_hogemails_med(session):
    AddressFactory()
    AddressFactory(email_address='address_2@hogemali.com')
    AddressFactory(email_address='address_3@hogemailcom')
    result = is_hogemails(session)
    assert not result