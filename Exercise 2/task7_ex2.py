
class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name:str, species:str, year_of_birth:int):
    return Pet(name, species, year_of_birth)

woofie = new_pet("Woofie", "Dachshund", 2015)

print(f"New dog called {woofie.name} which is a {woofie.species} and was born in {woofie.year_of_birth}")