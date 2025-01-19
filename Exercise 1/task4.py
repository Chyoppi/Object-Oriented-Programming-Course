#4. Write a program which repeatedly reads integers until the user enters 0. Print out the number of negative integers. Use functions in your solution.

int_list = []

#Another list to get all the negative integers
minus_int = []

#Function to let user put inputs
def List_loop():
    loop = False

    while loop != True:
        user_input = int(input("Give integer values [0 TO EXIT] "))
        if user_input == 0:
            break
        else:
            int_list.append(user_input)
    print(int_list)

#Goes through the list that user gave and prints out negative numbers from another list.
def Negative_integers():
    for x in int_list:
        if x < 0:
            minus_int.append(x)
    print(minus_int)

List_loop()
Negative_integers()