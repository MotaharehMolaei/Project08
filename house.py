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
        print(f"{self.id},{self.address}, {self.region}, {self.has_elevator}, {self.has_parking}, {self.has_storage}, {self.rooms} saved")


