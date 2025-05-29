import re

class Validator:
    def __init__(self, address, house_date):
        self.address = address
        self.house_date = house_date

    def is_valid_address(self):
        return bool(re.match(r'^[a-zA-Zآ-ی0-9\s\-,]{10,100}$', self.address))

# (id[0], address[1], region[2], has_elevator[3], has_parking[4], has_storage[5], rooms[6])
    def validate(self):
        errors = []

    # Validate ID
        if not (type(self.house[0]) == int and self.house[0] > 0):
            errors.append("House ID must be a positive integer.")

    # Validate Address
        if not address_validator(self.house[1]):
            errors.append("Address is invalid.")

    # Validate Region
        if not (type(self.house[2]) == str and re.match(r"^[a-zA-Zآ-ی0-9\s\-,]{3,50}$", self.house[2])):
            errors.append("Region name is invalid. English and persian letters and spaces are allowed.")

    # Validate Room count
        if not (type(self.house[6]) == int and self.house[6] > 0):
            errors.append("Room count must be a positive integer.")

        return errors

