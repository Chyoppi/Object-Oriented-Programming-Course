from wolf import Wolf
from random import randint
from time import sleep


class Dog(Wolf):
    def __init__(self, name):
        Wolf.__init__(self, "Domesticated")
        assert isinstance(name, str), "Must be string!"
        assert len(name) > 0, "Name must be atleast 1 letter long!"
        self.__name = name

    def make_sound(self):
        print("*Bork bork*")

    #method1
    def take_outside(self):
        action = randint(1,3)

        if action == 1:
            print(f"*{self.__name} pees*")

        elif action == 2:
            print(f"*{self.__name} poops*")

        else:
            print(f"*{self.__name} was too lazy to go outside*")

    #method2
    def throw_ball(self):
        print("*Ball gets thrown*")
        sleep(2)
        print(f"*{self.__name} running towards the ball*")
        sleep(2)
        print(f"*{self.__name} cam back with the ball*")

    #Encapsulation getter
    def get_name(self):
        return self.__name

    #Encasuplation setter
    def set_name(self, name):
        self.__name = name