import sqlalchemy
from sqlalchemy import orm

import pytest
from models import Base, User, Address

SESSION = orm.scoped_session(orm.sessionmaker())
BOUND = False


def pytest_addoption(parser):
    parser.addoption('--small_only', action='store_true')


def pytest_configure(config):
    config.addinivalue_line('markers', 'small: Small test')


def pytest_runtest_setup(item):

    small_only = item.config.getoption('small_only')
    if not small_only:
        global SESSION, BOUND
        if not BOUND:
            engine = sqlalchemy.create_engine('sqlite://')
            setup_tables(engine)
            SESSION.configure(bind=engine)
            BOUND = True

    small = item.get_closest_marker('small')
    if small_only and not small:
        pytest.skip('Skip medium/large test')


def setup_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return
