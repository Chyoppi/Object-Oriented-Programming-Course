from animal import Animal
from mammal import Mammal
from wolf import Wolf
from bird import Bird
from dog import Dog

def run_a_tests():
    a1 = Animal(6) # an insect?
    a2 = Animal(4) # a cow?
        
    a1.make_sound()
    print(a1.number_of_legs())

    a2.make_sound()
    print(a2.number_of_legs())



def run_b_tests():
    
    a3 = Mammal()
    a4 = Bird()
    ### aaa = Animal()
    wolf1 = Wolf("Raasinkorpi")
        
    #a3.make_sound()
    make_it_do_the_sound(a3)
    make_it_do_the_sound(a4)
    make_it_do_the_sound22(a4)
    ### make_it_do_the_sound22(aaa)
    make_it_do_the_sound(wolf1)

    wolf1.another_make_sound()
    print(a3.number_of_legs())


def make_it_do_the_sound(any_animal:Animal):
    any_animal.make_sound()


def make_it_do_the_sound22(any_bird:Bird):
    any_bird.make_sound()



def run_c_tests():
    a4 = Wolf("Raasinkorpi")
        
    a4.make_sound()
    print(a4.number_of_legs())



def run_d_tests():
    a5 = Bird()
        
    a5.make_sound()
    print(a5.number_of_legs())



print("a-tests:")
run_a_tests()



print()
print("b-tests:")
run_b_tests()

"""
print()
print("c-tests:")
run_c_tests()

print()
print("d-tests:")
run_d_tests()
"""

#Homework task 2 // test 1
#Added eat method to all classes
def run_d_tests():
    koira = Wolf("Salama")
    lintu = Bird()
    elain = Animal(4)
        
    koira.eat()
    lintu.eat()
    elain.eat()

run_d_tests()

#Homework task 3 // test 2
#Testing encapsulation
def run_e_tests():
    koira = Wolf("Salama")
    koira.set_pack_name("Kuusela")
    print(koira.get_pack_name())  

run_e_tests()

#Homework task 4 // test 3
#Encapsulation and inheritance
def run_f_tests():
    elain = Animal(4)
        
    print(elain.number_of_legs())

run_f_tests()

#Homework task 5 & 6
#Dog class with take_outside method and encapsulated info.
def run_g_tests():
    Hauvva = Dog("Hauvva")
    print(Hauvva.get_name())
    #Feature  1
    Hauvva.take_outside()

    #Feature 2
    Hauvva.throw_ball()

run_g_tests()

#Homework task 7

def run_h_tests():
    a10 = Animal(0)
    a10 = Animal("Pete")

run_h_tests()