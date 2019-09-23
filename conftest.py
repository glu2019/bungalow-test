import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture(scope="session")
def django_db_setup():
    """ Avoid creating/setting up the test database.
    The local database is used and transactions are not commited to the database """
    pass

@pytest.fixture()
def create_test_user(db, django_db_setup):
    
    user_data = {
        "username": "test",
        "is_superuser": True,
        "first_name": "Guangwen",
        "last_name": "Lu",
        "email": "test@gmail.com",
        "is_active": True 
    }
    user = User.objects.create(**user_data)
    user.set_password("test_password")
    user.save()
    return user

@pytest.fixture()
def set_client_authentication(db, django_db_setup, create_test_user):
    client = APIClient()
    client.login(username="test", password="test_password")
    return client