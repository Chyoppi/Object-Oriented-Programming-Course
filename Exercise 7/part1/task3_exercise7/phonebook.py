from person import Person

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_number(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name].get_numbers()
    
    def set_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].set_address(address)

    def number_search(self, number: str):
        for name, person in self.__persons.items():
            if number in person.get_numbers():
                return name
        return None

    def all_entries(self):
        return {name: person.get_numbers() for name, person in self.__persons.items()}

# code for testing
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
phonebook.add_number("Eric", "02-654321")
phonebook.add_number("Emily", "03-987654")

print(phonebook.get_numbers("Eric"))  # Output: ['02-123456', '02-654321']
print(phonebook.get_numbers("Emily"))  # Output: ['03-987654']
print(phonebook.get_numbers("John"))  # Output: None

print(phonebook.number_search("02-123456"))  # Output: Eric
print(phonebook.number_search("03-987654"))  # Output: Emily
print(phonebook.number_search("04-000000"))  # Output: None

print(phonebook.all_entries())