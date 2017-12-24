
class Garage:

    def __init__(self, garage_id, owner, admins, vehicles):
        self.garage_id = garage_id
        self.owner = owner
        self.admins = admins
        self.vehicles = vehicles

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
