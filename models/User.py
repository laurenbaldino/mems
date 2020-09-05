from sqlalchemy import Column, Integer, String
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    email = Column(String)
