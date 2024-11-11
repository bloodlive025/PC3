import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.userService import UserService
from src.user import User
import pytest





def test_register_user():
    user_service = UserService()
    user = user_service.register_user("Juan", "password")
    assert user.username == "Juan"
def test_register_duplicate_user():
    user_service = UserService()
    user = user_service.register_user("user2","pasword2")
    user = user_service.register_user("user2","pasword3")
    assert len(user_service.users) == 1

def tests_register_diferent_user():
    user_service = UserService()
    user = user_service.register_user("user2","pasword2")
    user = user_service.register_user("user3","pasword3")
    assert len(user_service.users) == 2

def test_autentificate_User():
    user_service = UserService()
    user = user_service.register_user("Juan", "password")
    assert user_service.authenticate_user("Juan", "password") == user
