#4. Write a program which repeatedly reads integers until the user enters 0. Print out the number of negative integers. Use functions in your solution.

int_list = []

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

#Goes through the list that user gave and prints out negative numbers.
def Negative_integers():
    print("Negative numbers:")
    for x in int_list:
        if x < 0:
            print(x)

#Checks if number is even and if it is prints it.
def Even_integers():
    print("Even numbers:")
    for x in int_list:
        if x % 2 == 0:
            print(x)

List_loop()
Negative_integers()
Even_integers()