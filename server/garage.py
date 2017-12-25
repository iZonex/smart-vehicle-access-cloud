import logging
from .vehicle import Vehicle

logger = logging.getLogger(__name__)


class GarageAdmins:

    def __init__(self, garage_id):
        pass

    def remove(self, user_id):
        pass

    def add(self, user_id):
        pass

    def all(self):
        pass


class GarageVehicles:

    def __init__(self, garage_id):
        self.garage_id = garage_id
        self._load_vehicles()

    def _load_vehicles(self):
        self.vehicles = Vehicle.get_garage(self.garage_id)

    def get_vehicle(self, vehicle_id):
        return self.vehicles.get(vehicle_id)

    def remove_vehicle(self, vehicle_id):
        try:
            del self.vehicles[vehicle_id]
        except KeyError as err:
            logger.error(f'Vehicle {vehicle_id} in garage: {self.garage_id} not found')


class Garage:

    def __init__(self, name, owner):
        self._id = None
        self.name = name
        self.owner = owner

    @classmethod
    def get_user_garage(cls, user_id):
        pass

    def get_admins(self):
        GarageAdmins(self._id)

    def get_vehicles(self):
        GarageVehicles(self._id)
