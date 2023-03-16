from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H;%M:%S"))

USER = {
    "1000": {
        "user_id": "1000",
        "user_name": "Caio Rolando da Rocha",
        "user_email": "teste@gmail.com",
        "user_password": "123",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
    "2000": {
        "user_id": "2000",
        "user_name": "Jucimar Maia da Silva Jr",
        "user_email": "teste@gmail.com",
        "user_password": "123",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
    "3000": {
        "user_id": "3000",
        "user_name": "Guilherme Correia Tapajós",
        "user_email": "teste@gmail.com",
        "user_password": "123",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
    "4000": {
        "user_id": "4000",
        "user_name": "Arthur Uguen de Mendonça",
        "user_email": "teste@gmail.com",
        "user_password": "123",
        "user_status": "0",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    return list(USER.values())

def create(user):
    user_id = user.get("user_id")
    user_name = user.get("user_name", "")
    user_email = user.get("user_email")
    user_password = user.get("user_password")

    if user_id and user_id not in USER:
        USER[user_id] = {
            "user_id": user_id,
            "user_name": user_name,
            "user_email": user_email,
            "user_password": user_password,
            "user_status": "0",
            "timestamp": get_timestamp(),
        }
        return USER[user_id], 201
    else:
        abort(
            406,
            f"User with last name {user_id} already exists",
        )

def update(user_id, user):
    if user_id in USER:
        USER[user_id]["user_name"] = user.get("user_name", USER[user_id]["user_name"])
        USER[user_id]["user_email"] = user.get("user_email", USER[user_id]["user_email"])
        USER[user_id]["user_password"] = user.get("user_password", USER[user_id]["user_password"])
        USER[user_id]["user_status"] = user.get("user_status", USER[user_id]["user_status"])
        USER[user_id]["timestamp"] = get_timestamp()
        return USER[user_id]
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )

def read_one(user_id):
    if user_id in USER:
        return USER[user_id]
    else:
        abort(
            404,
            f"Person with ID {user_id} not found",
        )
