class Animal:

    def __init__(self, number_of_legs):
        assert isinstance(number_of_legs, int), "Must be integer"
        assert number_of_legs > 0, "Must be positive"
        self.__legs = number_of_legs

    def number_of_legs(self): 
        return self.__legs

    def make_sound(self):
        print("*it's quiet*")

    def eat(self):
        print("*munch munch*")

        
        