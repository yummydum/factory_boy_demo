import pytest
from models import User, Address
from app import get_addresses, is_hogemails
from conftest import SESSION


@pytest.fixture()
def session():
    yield SESSION
    SESSION.rollback()


def test_get_addresses(session):

    # Add user
    user1 = User(name='name_1', fullname='fullname_1', nickname='nickname_1')
    user2 = User(name='name_2', fullname='fullname_2', nickname='nickname_2')
    user3 = User(name='name_3', fullname='fullname_3', nickname='nickname_3')

    for user in [user1, user2, user3]:
        session.add(user)

    # Add address
    address1 = Address(email_address='address_1@hogemail.com',
                       user_id=user1.user_id,
                       user=user1)
    address2 = Address(email_address='address_2@hogemail.com',
                       user_id=user2.user_id,
                       user=user2)
    address3 = Address(email_address='address_3@hogemail.com',
                       user_id=user3.user_id,
                       user=user3)

    for address in [address1, address2, address3]:
        session.add(address)

    # Execute test
    result = get_addresses(session)
    assert len(result) == 3


def test_is_hogemail(session):
    # Add user
    user1 = User(name='name_1', fullname='fullname_1', nickname='nickname_1')
    user2 = User(name='name_2', fullname='fullname_2', nickname='nickname_2')
    user3 = User(name='name_3', fullname='fullname_3', nickname='nickname_3')

    for user in [user1, user2, user3]:
        session.add(user)

    # Add address
    address1 = Address(email_address='address_1@hogemail.com',
                       user_id=user1.user_id,
                       user=user1)
    address2 = Address(email_address='address_2@hogemali.com',
                       user_id=user2.user_id,
                       user=user2)
    address3 = Address(email_address='address_3@hogemailcom',
                       user_id=user3.user_id,
                       user=user3)

    for address in [address1, address2, address3]:
        session.add(address)

    # Execute test
    result = is_hogemails(session)
    assert not result