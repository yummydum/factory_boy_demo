from factories import AddressFactory
from app import get_address, check_emails


def test_address():
    AddressFactory()
    AddressFactory()
    AddressFactory()
    get_address()


def test_check_emails():
    AddressFactory()
    AddressFactory(email_address='user_2@gmailcom')
    AddressFactory(email_address='user_3gmail.com')
    check_emails()