#9. Code a function that returns a random number bet ween 1-6 when calling it. Print out the number where the function is called (so do not print the number inside the function). Name the function properly (see style guide).

import random

def generate_number():
    return random.randint(1,6)

def print_number():
    print(generate_number())

print_number()