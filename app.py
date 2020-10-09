from models import Address


def get_addresses(session):
    return session.query(Address).all()


def is_hogemails(session):
    data = get_addresses(session)
    for address in data:
        if not address.email_address.endswith('@hogemail.com'):
            return False
    return True
