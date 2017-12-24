from server.user_account import User
import pytest


@pytest.mark.parametrize(
    'user_id', 'first_name', 'second_name', 'middle_name',
    'full_name', 'email', 'country', 'city', 'address',
    'zip', 'phone_number', 'password', [
        ('1', 'Ivan', 'Ivan', 'Ivanov', 'Ivan Ivanovich Ivanov',
         'test@gmail.com', 'Ukraine', 'Kyiv', 'Anotonovicha 1',
         '00135', '+380939999999', 'hash')
])
def test_user_init(user_id, first_name, second_name, middle_name,
                   full_name, email, country, city, address, zip,
                   phone_number, password):
    obj = User(user_id, first_name, second_name, middle_name,
               full_name, email, country, city, address, zip,
               phone_number, password)
    assert isinstance(obj, User)
