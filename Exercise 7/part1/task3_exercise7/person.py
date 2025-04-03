class Person():
    def __init__(self, name):
        self.name = name
        self.numbers = []
        self.address = None
        
    def add_number(self, number):
        self.numbers.append(number)

    def add_address(self, address):
        self.address = address

    def get_numbers(self):
        return self.numbers

person = Person("Eric")
print(person.name)
print(person.numbers)
print(person.address)
person.add_number("040-123456")
person.add_address("Mannerheimintie 10 Helsinki")
print(person.numbers)
print(person.address)