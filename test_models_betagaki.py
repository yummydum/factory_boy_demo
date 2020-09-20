from models import User, Address
from app import get_address, check_emails


def test_get_address(session):

    # Add user
    user1 = User(name='name_1', fullname='fullname_1', nickname='nickname_1')
    user2 = User(name='name_2', fullname='fullname_2', nickname='nickname_2')
    user3 = User(name='name_3', fullname='fullname_3', nickname='nickname_3')

    for user in [user1, user2, user3]:
        session.add(user)
    session.commit()

    # Add address
    address1 = Address(email_address='address_1@gmail.com',
                       user_id=user1.user_id,
                       user=user1)
    address2 = Address(email_address='address_2.com',
                       user_id=user2.user_id,
                       user=user2)
    address3 = Address(email_address='address_3.com',
                       user_id=user3.user_id,
                       user=user3)

    for address in [address1, address2, address3]:
        session.add(address)
    session.commit()

    # Execute test
    get_address()


def test_check_email(session):
    # Add user
    user1 = User(name='name_1', fullname='fullname_1', nickname='nickname_1')
    user2 = User(name='name_2', fullname='fullname_2', nickname='nickname_2')
    user3 = User(name='name_3', fullname='fullname_3', nickname='nickname_3')

    for user in [user1, user2, user3]:
        session.add(user)
    session.commit()

    # Add address
    address1 = Address(email_address='address_1@gmail.com',
                       user_id=user1.user_id,
                       user=user1)
    address2 = Address(email_address='address_2.com',
                       user_id=user2.user_id,
                       user=user2)
    address3 = Address(email_address='address_3.com',
                       user_id=user3.user_id,
                       user=user3)

    for address in [address1, address2, address3]:
        session.add(address)
    session.commit()

    # Execute test
    check_emails()