import re

class House:
    def __init__(self, id, address, region, has_elevator, has_parking, has_storage, rooms):
        self.id = id
        self.address = address
        self.region = region
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.has_storage = has_storage
        self.rooms = rooms

    def save_house(self):
        print(
            f"{self.id},{self.address}, {self.region}, {self.has_elevator}, {self.has_parking}, {self.has_storage}, {self.rooms} saved")

    def address_validator(self):
        return bool(re.match(r'^[a-zA-Zآ-ی0-9\s\-,]{10,100}$', self.address))

    def validate(self):
        errors = []

        if not (type(self.id) == int and self.id > 0):
            errors.append("House ID must be a positive integer.")

        if not self.address_validator():
            errors.append("Address is invalid.")

        if not (type(self.region) == str and re.match(r"^[a-zA-Zآ-ی0-9\s\-,]{3,50}$", self.region)):
            errors.append("Region name is invalid. English and Persian letters and spaces are allowed.")

        if not (type(self.rooms) == int and self.rooms > 0):
            errors.append("Room count must be a positive integer.")

        return errors

