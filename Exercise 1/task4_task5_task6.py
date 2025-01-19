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

#5. Add a function to the previous task that counts the number of even integers (= parilliset luvut in Finnish) that were among the entered
#Checks if number is even and if it is adds +1 to even value.
def Even_integers():
    even_value = 0
    for x in int_list:
        if x % 2 == 0:
            even_value += 1
    print(f"Amount of even numbers: {even_value}")

#6. Add to the previous task a function that counts the sum of the positive integers divisible by three. 
def Sum_of_three():
    print("Sum of values which are divisible by 3")
    sum_three = 0
    for x in int_list:
        if x % 3 == 0:
            if x > 0:
                sum_three += x
    print(f"Sum: {sum_three}")

List_loop()
Negative_integers()
Even_integers()
Sum_of_three()