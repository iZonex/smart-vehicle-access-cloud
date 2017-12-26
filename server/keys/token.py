import logging

logger = logging.getLogger(__name__)

class VehicleToken:

    def __init__(self, user_id, vehicle_id, expired):
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.expired = expired

    def create_token(self):
        pass

    def revoke_token(self):
        pass

    def all_tokens(self):
        pass

    def get_token(self):
        pass
