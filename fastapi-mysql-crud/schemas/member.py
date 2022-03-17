from pydantic import BaseModel


class Member(BaseModel):
    firstname: str
    lastname: str
    mobile: int
    email: str
    password: str
    adhaar: str
