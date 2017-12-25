
class VehicleDescription:
    pass


class Vehicle:

    def __init__(self, vehicle_id, owner_id, manufacture,
                 vehicle_type, year_of_manufacture, first_registration,
                 vehicle_identification_number, registration_number):
        self.vehicle_id = vehicle_id
        self.owner_id = owner_id
        self.manufacture = manufacture
        self.vehicle_type = vehicle_type
        self.year_of_manufacture = year_of_manufacture
        self.first_registration = first_registration
        self.vehicle_identification_number = vehicle_identification_number
        self.registration_number = registration_number