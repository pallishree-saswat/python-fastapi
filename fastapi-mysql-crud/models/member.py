
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

members = Table(
    "members", meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(255)),
    Column('lastname', String(255)),
    Column('mobile', Integer),
    Column('email', String(255)),
    Column('password', String(255)),
    Column('adhaar', String(255))
)

meta.create_all(engine)
