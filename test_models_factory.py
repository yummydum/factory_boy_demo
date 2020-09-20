from factories import AddressFactory
from app import get_address, check_emails


def test_address():
    AddressFactory.create_batch(3)
    result = get_address()
    assert len(result) == 3


def test_check_emails():
    AddressFactory()
    AddressFactory(email_address='user_2@gmailcom')
    AddressFactory(email_address='user_3gmail.com')
    result = check_emails()
    assert not result