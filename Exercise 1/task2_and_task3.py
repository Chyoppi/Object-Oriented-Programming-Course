#2. Code a list of at least 10 items and fill it with numbers asked from user. Do the same with strings. Print out both lists. Then fill the number list with randomly generated numbers and print it out. 
import random

number_list=[]
string_list=[]

#Number_list part, it asks user 10 times something to add to list until it stops.
number_loop = False
while number_loop != True:
    number_input = int(input("Give 10 numbers to add to list [0 TO EXIT]: "))
    if len(number_list) == 10:
        break

    elif number_input == 0:
        break
    
    else:
        number_list.append(number_input)
print(number_list)

#String_list part, it asks user 10 times something to add to list until it stops.
string_loop = False
while string_loop != True:
    string_input = str(input("Give 10 strings to add to list [None INPUT TO EXIT]: "))
    if len(string_list) == 10:
        break

    elif string_input == "None":
        break
    
    else:
        string_list.append(string_input)
print(string_list)

#Lets user decide how many random numbers will be added to number_list
value = int(input("How many random numbers do you want to add to your numbers list: "))

while value != 0:
    random_number = random.randint(1,1000)
    number_list.append(random_number)
    value -= 1
print(number_list)

#3. Arrange numbers in the list from smallest to largest and strings in alphabetical order and print out the lists. 
number_list.sort()
string_list.sort()
print(number_list)
print(string_list)