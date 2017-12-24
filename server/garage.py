

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
        pass

    def remove(self, user_id):
        pass

    def add(self, user_id):
        pass

    def all(self):
        pass


class Garage:

    def __init__(self, garage_id, owner, admins, vehicles):
        self.garage_id = garage_id
        self.owner = owner
        self.admins = GarageAdmins(garage_id)
        self.vehicles = GarageVehicles(garage_id)

    @classmethod
    def get_garage(cls, garage_id):
        pass

    def get_admins(self):
        pass

    def add_admins(self, user):
        pass

    def remove_admins(self, user):
        pass

    def add_vehicles(self, vehicle):
        pass

    def remove_vehicles(self, vehicle):
        pass

    def get_vehicles(self):
        pass
