from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user
from routes.member import member
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


app.include_router(user)
app.include_router(member)
