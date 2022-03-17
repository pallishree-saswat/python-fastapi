from fastapi import APIRouter
from config.db import conn
from models.member import members
from schemas.member import Member
from sqlalchemy import func, select

from cryptography.fernet import Fernet

member = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)


@member.post('/signup')
async def signup(member: Member):
    new_member = {"firstname": member.firstname,
                  "lastname": member.lastname, "email": member.email,
                  "mobile": member.mobile, "adhaar": member.adhaar, }
    new_member["password"] = f.encrypt(member.password.encode("utf-8"))
    result = conn.execute(members.insert().values(new_member))
    return conn.execute(members.select().where(members.c.id == result.lastrowid)).first()


@member.post('/login')
async def signup(member: Member):
    new_member = { "email": member.email}
    member = conn.execute(members.select().where(members.c.email == member.email)).fetchall()
    new_member["password"] = f.encrypt(member.password.encode("utf-8"))
    result = conn.execute(members.insert().values(new_member))
    return conn.execute(members.select().where(members.c.id == result.lastrowid)).first()
