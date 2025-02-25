
class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} g)"

class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        total_weight = 0
        for present in self.presents:
            total_weight += present.weight
        return total_weight

game = Present("Minecraft", 64)
print("The present is a", game.name)
print("The present weighs", game.weight, "g")
print("Present:", game)
lego= Present("Lego", 100)

box = Box()
box.add_present(game)
print(box.total_weight())

box.add_present(lego)
print(box.total_weight())