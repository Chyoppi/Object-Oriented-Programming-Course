from carriage_class import Carriage

class Train:
    def __init__(self, id):
        self.id = id
        self.carriages = []

    #List of carriages in train by id
    def list_carriages(self):
        return [carriage.id for carriage in self.carriages]

    #Adding and removing carriages and also sort whenever adding new carriage
    def add_carriage(self, carriage):
        self.carriages.append(carriage)
        self.carriages.sort(key=lambda x: x.id)

    def remove_carriage(self, carriage_id):
        for carriage in self.carriages:
            if carriage.id == carriage_id:
                self.carriages.remove(carriage)
                break

    #Reserve/remove seat in carriage
    def reserve_seat(self, carriage_id, seat_number):
        for carriage in self.carriages:
            if carriage.id == carriage_id:
                carriage.reserve_seat(seat_number)
                print(f"Seat from carriage: {carriage.id} and seat number: {seat_number} is reserved")
                return
        print("No such carriage")

    def remove_reservation(self, carriage_id, seat_number):
        for carriage in self.carriages:
            if carriage.id == carriage_id:
                carriage.remove_reservation(seat_number)
                print(f"Seat from carriage: {carriage.id} and seat number: {seat_number} is removed")
                return
        print("No such carriage")

    #Show train with carriages
    def show_train(self):
        print("Train ID:", self.id)
        print("Carriages:")
        for carriage in self.carriages:
            print(f"Carriage ID: {carriage.id}")
            carriage.report()
            print("--------------------")

#Creating carrigaes and train
carriage1 = Carriage(1, 10)
carriage2 = Carriage(2, 10)
carriage5 = Carriage(5, 10)
carriage3 = Carriage(3, 10)
train1 = Train(1)

#Testing adding and removing carriages
train1.add_carriage(carriage1)
train1.add_carriage(carriage5)
train1.add_carriage(carriage2)
train1.add_carriage(carriage3)
print(train1.list_carriages())

train1.remove_carriage(2)
print(train1.list_carriages())

#Reserving seat in carriage
train1.reserve_seat(1, 5)

#Testing with invalid carriage id
train1.reserve_seat(4, 5)

#Show train with carriages
show_train = train1.show_train()

#Removing reservation from carriage
train1.remove_reservation(1, 5)
show_train = train1.show_train()