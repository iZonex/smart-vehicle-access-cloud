
class UserProfile:

    def __init__(self, user_id, country, city, address, zip,
                 phone_number):
        self.country = country
        self.city = city
        self.address = address
        self.zip = zip
        self.phone_number = phone_number


class UserPhoto:

    def __init__(self, user_id):
        pass


class User:

    def __init__(self, user_id, first_name, second_name, middle_name,
                 full_name, email):
        self.user_id = user_id
        self.first_name = first_name
        self.second_name = second_name
        self.middle_name = middle_name
        self.full_name = full_name
        self.email = email

    def set_password(self, password):
        pass

    def reset_password(self):
        pass

    def check_password(self):
        pass
