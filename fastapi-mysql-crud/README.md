# Fastapi MySQL REST API

Setup env

```
virtualenv venv
```

For Linux/Mac

```
source venv/bin/activate
```

For Windows

```
source venv/Scripts/activate
```

Install package

```
pip install fastapi  uvicorn pymysql sqlalchemy
```

Start server

```
uvicorn index:app --reload
```
