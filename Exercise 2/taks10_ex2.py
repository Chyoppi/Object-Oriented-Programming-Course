

class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    #Part 1, return True if the property is bigger than the one compared to
    def bigger(self, comapared_to):
        return self.square_metres > comapared_to.square_metres
    
    #Part 2, return the difference in price between the two properties
    def price_difference(self, compared_to):
        return abs(self.square_metres * self.price_per_sqm - compared_to.square_metres * compared_to.price_per_sqm)
    
    #Part 3, return True if the property is more expensive than the one compared to
    def more_expensive(self, compared_to):
        return self.price_per_sqm > compared_to.price_per_sqm

#Testing that the method works correctly
central_studio = RealProperty(1, 16, 5500)
downtown_two_bedroom = RealProperty(2, 38, 4200)
suburbs_three_bedroom = RealProperty(3, 78, 2500)

print(central_studio.more_expensive(downtown_two_bedroom))
print(suburbs_three_bedroom.bigger(downtown_two_bedroom))
print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))