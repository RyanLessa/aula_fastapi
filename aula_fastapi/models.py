from .database import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = 'groups'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    name = sa.Column(sa.String, unique=True)

    users = relationship('User', back_populates='group')


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'))

    username = sa.Column(sa.String, unique=True, nullable=False)

    group = relationship('Group', back_populates='users')


class Migrations:
    @classmethod 
    def migrations(cls, engine):
        Base.metadata.create_all(engine)
