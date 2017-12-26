import logging

logger = logging.getLogger(__name__)

class VehicleKey:

    def __init__(self, user_id, vehicle_id, expired):
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.expired = expired

    def create_key(self):
        pass

    def revoke_key(self):
        pass

    def all_keys(self):
        pass

    def get_key(self):
        pass
