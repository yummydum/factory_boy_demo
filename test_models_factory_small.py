import pytest
from factories import AddressFactory
from app import get_address, check_emails


@pytest.mark.small
def test_address():
    AddressFactory.build_batch(3)
    result = get_address()
    assert len(result) == 3


@pytest.mark.small
def test_check_emails():
    AddressFactory.build()
    AddressFactory.build(email_address='user_2@gmailcom')
    AddressFactory.build(email_address='user_3gmail.com')
    result = check_emails()
    assert not result


def test_check_emails_med():
    AddressFactory()
    AddressFactory(email_address='user_2@gmailcom')
    AddressFactory(email_address='user_3gmail.com')
    result = check_emails()
    assert not result