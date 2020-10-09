import pytest
from factories import AddressFactory
from app import get_addresses, is_hogemails
from conftest import SESSION


@pytest.fixture()
def session():
    yield SESSION
    SESSION.rollback()


def test_address(session):
    AddressFactory.create_batch(3)
    result = get_addresses(session)
    assert len(result) == 3


def test_is_hogemails(session):
    AddressFactory()
    AddressFactory(email_address='address_2@hogemali.com')
    AddressFactory(email_address='address_3@hogemailcom')
    result = is_hogemails(session)
    assert not result