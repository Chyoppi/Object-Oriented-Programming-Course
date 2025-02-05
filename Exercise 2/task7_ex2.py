# Write a class called Pet that has three attributes: name, species, and year_of_birth.

class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

# Function named new_pet(name: str, species: str, year_of_birth: int) outside the class definition. The function should create and return a new object of type Pet, as defined in the class Pet
def new_pet(name:str, species:str, year_of_birth:int):
    return Pet(name, species, year_of_birth)

woofie = new_pet("Woofie", "Dachshund", 2015)

print(f"New dog called {woofie.name} which is a {woofie.species} and was born in {woofie.year_of_birth}")