from sqlalchemy import Table,Column,String,Integer
from config.db import meta

users = Table(
    'users',meta,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('name',String(50)),
    Column('email',String(225),unique=True),
    Column('password',String(225)),

)