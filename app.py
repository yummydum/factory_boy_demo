from models import User, Address


def get_address(session):
    return session.query(Address).all()


def is_gmails(session):
    data = get_address(session)
    for address in data:
        if not address.email_address.endswith('@gmail.com'):
            return False
    return True