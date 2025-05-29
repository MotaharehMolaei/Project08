import re

class Validator:
    def address_validator(address):
        return re.match(r'^[a-zA-Zآ-ی0-9\s\-,]{10,100}$', address)



# (id[0], address[1], region[2], has_elevator[3], has_parking[4], has_storage[5], rooms[6])
def house_validator(house):
    errors = []

    # Validate ID
    if not (type(house[0]) == int and house[0] > 0):
        errors.append("House ID must be a positive integer.")

    # Validate Address
    if not address_validator(house[1]):
        errors.append("Address is invalid.")

    # Validate Region
    if not (type(house[2]) == str and re.match(r"^[a-zA-Zآ-ی0-9\s\-,]{3,50}$", house[2])):
        errors.append("Region name is invalid. English and persian letters and spaces are allowed.")

    # Validate Room count
    if not (type(house[6]) == int and house[6] > 0):
        errors.append("Room count must be a positive integer.")

    return errors
