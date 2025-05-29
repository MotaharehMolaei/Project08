import re


def house_validator(house):
    errors = []

    if not (type(house.id) == int and house.id > 0):
        errors.append("House ID must be a positive integer.")

    if not bool(re.match(r'^[a-zA-Zآ-ی0-9\s\-,]{10,100}$', house.address)):
        errors.append("Address is invalid.")

    if not (type(house.region) == str and re.match(r"^[a-zA-Zآ-ی0-9\s\-,]{3,50}$", house.region)):
        errors.append("Region name is invalid. English and Persian letters and spaces are allowed.")

    if not (type(house.rooms) == int and house.rooms > 0):
        errors.append("Room count must be a positive integer.")

    return errors