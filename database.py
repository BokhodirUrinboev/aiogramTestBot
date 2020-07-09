from aiogram import types, Bot
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql

from data.config import db_pass, db_user, host

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(2))
    full_name = Column(String(100))
    username = Column(String(50))
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)


class Mobile(db.Model):
    __tablename__ = 'mobile'
    query: sql.Select

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    number = Column(BigInteger)
    password = Column(String(100))

    def __repr__(self):
        return "<Mobile(user_id='{}', number='{}',password='{}')>".format(
            self.user_id, self.number, self.password)


class Internet(db.Model):
    __tablename__ = 'internet'
    query: sql.Select

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    login = Column(BigInteger)
    password = Column(String(100))

    def __repr__(self):
        return "<Internet(user_id='{}', number='{}',password='{}')>".format(
            self.user_id, self.number, self.password)



class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name

        await new_user.create()
        return new_user

    async def set_language(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()

    async def count_users(self) -> int:
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def check_referrals(self):
        bot = Bot.get_current()
        user_id = types.User.get_current().id

        user = await User.query.where(User.user_id == user_id).gino.first()
        mob_referrals = await Mobile.query.where(Mobile.id == user.user_id).gino.all()
        internet_referrals =await Internet.query.where(Internet.id == user.user_id).all()
        referrals = [mob_referrals, internet_referrals]
        return referrals

    async def get_mobile(self, user_id):
        mobile = await Mobile().query.where(Mobile.user_id == user_id).gino.all()
        return mobile

    async def get_internet(self, user_id):
        mobile = await Internet().query.where(Mobile.user_id == user_id).gino.all()
        return mobile

    async def check_attachment(self, user_id):
        if await self.get_internet(user_id) or await self.get_mobile(user_id):
            return True
        else:
            return False

    async def attach_mobile(self, user_id, number, password):
        new_mobile = Mobile()
        new_mobile.user_id = user_id
        new_mobile.number = number
        new_mobile.password = password
        await new_mobile.create()
        return new_mobile

    async def attach_internet(self, user_id, login, password):
        new_internet = Internet()
        new_internet.user_id = user_id
        new_internet.login = login
        new_internet.password = password
        await new_internet.create()
        return new_internet


async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/uztelecom')

    # Create tables
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()
