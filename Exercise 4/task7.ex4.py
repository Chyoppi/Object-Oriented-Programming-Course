class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class Room:
    def __init__ (self):
        self.persons = []

    def add_person(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False
    
    def print_contents(self):
        print("The room contains the following persons:")
        for person in self.persons:
            print(f"{person.name} {person.height} cm")

    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            short = self.persons[0]
            for person in self.persons:
                if person.height < short.height:
                    short = person
            return f"{short.name}, {short.height} cm"
    
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            short = self.persons[0]
            for person in self.persons:
                if person.height < short.height:
                    short = person
            self.persons.remove(short)
            return short

room = Room()
print("Is the room empty?", room.is_empty())
room.add_person(Person("Lea", 183))
room.add_person(Person("Kenya", 175))
room.add_person(Person("Ally", 166))
room.add_person(Person("Mia", 170))
room.add_person(Person("Liam", 180))
print("Is the room empty?", room.is_empty())
room.print_contents()

print("Shortest:", room.shortest())
removed = room.remove_shortest()
print(f"Removed from room: {removed.name}") 
room.print_contents()