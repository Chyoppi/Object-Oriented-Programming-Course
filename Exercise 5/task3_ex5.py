
class Item:
    def __init__ (self, item_name:str, item_weight:int):
        self.item_name = item_name
        self.item_weight = item_weight

    def __str__(self):
        return self.item_name + " ("+str(self.item_weight) + "g)"

    def name(self):
        return self.item_name
    
    def weight(self):
        return self.item_weight

book = Item("ABC Book", 200)   
phone = Item("Nokia 3210", 100) 
print("Name of the book:", book.name())   
print("Weight of the book:", book.weight()) 
print("Book:", book) 
print("Phone:", phone)

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item: Item):
        if self.weight() + item.item_weight <= self.max_weight:
            self.items.append(item)
        else:
            print("Suitcase is full")

    def print_items(self):
        for item in self.items:
            print(item.name(), item.weight(), "g")

    def weight(self):
        return sum(item.item_weight for item in self.items)
    
    def heaviest_item(self):
        if len(self.items) == 0:
            return None
        else:
            self.items.sort
            return self.items[-1]

    def __str__(self):
        total_weight = self.weight()
        total_items = len(self.items)
        if total_items == 1:
            return f"{total_items} item ({total_weight} g)"
        else:
            return f"{total_items} items ({total_weight} g)"


book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400 ) 
suitcase = Suitcase(1000)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)
heaviest = suitcase.heaviest_item()
print(f"The heaviest item: {heaviest}")


class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight * 1000
        self.suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.max_weight:
            self.suitcases.append(suitcase)
        else:
            print("Cargo hold is full")

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.suitcases)
    
    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()

    def __str__(self):
        remaining_weight = (self.max_weight - self.weight()) / 1000
        return f"{len(self.suitcases)} suitcases, space for {remaining_weight} kg more"


book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400 )
adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold = CargoHold(100  ) 
cargo_hold.add_suitcase(adas_suitcase) 
cargo_hold.add_suitcase(peters_suitcase)
print("The suitcases in the cargo hold contain the following items:") 
cargo_hold.print_items()
        