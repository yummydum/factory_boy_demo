from factory.alchemy import SQLAlchemyModelFactory
from factory import Faker, Sequence, SubFactory, Iterator, SelfAttribute
from models import User, Address
from conftest import make_session

Session = make_session()


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = 'commit'

    user_id = Sequence(lambda n: n)
    name = Sequence(lambda n: f'name_{n}')
    fullname = Sequence(lambda n: f'fullname_{n}')
    nickname = Sequence(lambda n: f'nickname_{n}')


class AddressFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Address
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = 'commit'

    address_id = Sequence(lambda n: n)
    email_address = Sequence(lambda n: f'address_{n}@gmail.com')
    user = SubFactory(UserFactory)
    user_id = SelfAttribute('user.user_id')