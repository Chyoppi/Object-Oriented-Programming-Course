class Carriage:
    def __init__(self, id, seats):
        self.id = id
        self.seats = seats
        self.reserved_seats = set()

    def reserve_seat(self, seat_number):
        if seat_number < 1 or seat_number > self.seats:
            print("Invalid seat number")
        if seat_number in self.reserved_seats:
            print("Seat already reserved")
        else:
            self.reserved_seats.add(seat_number)

    def remove_reservation(self, seat_number):
        if seat_number in self.reserved_seats:
            self.reserved_seats.remove(seat_number)
        else:
            print("Seat not reserved")

    def reset_reservations(self):
        self.reserved_seats.clear()

    def total_reservations(self):
        return len(self.reserved_seats)

    def get_reserved_seats(self):
        return sorted(self.reserved_seats)

    def is_full(self):
        if len(self.reserved_seats) == self.seats:
            print("Carriage is full")
        else:
            print("Carriage is not full")

    def report(self):
        reserved = sorted(self.reserved_seats)
        unreserved = sorted(set(range(1, self.seats + 1)) - self.reserved_seats)
        print(f"Reserved seats: {reserved}, Unreserved seats: {unreserved}")