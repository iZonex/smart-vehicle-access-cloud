import logging
from .garage import Garage
from .user_account import User

logger = logging.getLogger(__name__)

class AccessControl:

    def __init__(self, user_id):
        self.user = User.get_user(user_id)
        self.garage = Garage.get_user_garage(user_id)

    def get_vehicles(self):
        return self.garage.get()
