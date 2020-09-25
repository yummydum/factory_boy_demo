import pytest
from factories import AddressFactory
from app import get_address, is_gmails
from conftest import SESSION


@pytest.fixture()
def session():
    yield SESSION
    SESSION.rollback()


def test_address(session):
    AddressFactory.create_batch(3)
    result = get_address(session)
    assert len(result) == 3


def test_is_gmails(session):
    AddressFactory()
    AddressFactory(email_address='address_2@gmali.com')
    AddressFactory(email_address='address_3@gmailcom')
    result = is_gmails(session)
    assert not result