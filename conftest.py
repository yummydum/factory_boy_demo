import sqlalchemy
from sqlalchemy import orm

import pytest
from models import Base, User, Address


def make_session():
    engine = sqlalchemy.create_engine('sqlite://')

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = orm.scoped_session(orm.sessionmaker())
    session.configure(bind=engine)
    return session


@pytest.fixture(scope='session')
def session():
    yield make_session()
