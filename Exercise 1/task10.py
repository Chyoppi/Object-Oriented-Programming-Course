"""
10.Write a phone book application. It should work as follows:
    command (1 search, 2 add, 3 quit): 2
    name: peter
    number: 040-5466745
    ok!
    command (1 search, 2 add, 3 quit): 2
    name: emily
    number: 045-1212344
    ok!
    command (1 search, 2 add, 3 quit): 1
    name: peter
    040-5466745
    command (1 search, 2 add, 3 quit): 1
    name: maryno number
    command (1 search, 2 add, 3 quit): 2
    name: peternumber: 09-22223333
    ok!
    command (1 search, 2 add, 3 quit): 1
    name: peter
    09-22223333
    command (1 search, 2 add, 3 quit): 3
    quitting...
"""
phone_book = {}

def search_phone():
    name = input("Enter the name: ").strip()
    if name in phone_book:
        print(f"{name}'s number is {phone_book[name]}")
    else:
        print(f"{name} was not found in the phone book.")

def add_phone():
    name = input("Enter the name: ").strip()
    number = input("Enter the phone number: ").strip()
    if name in phone_book:
        print(f"{name} already exists. Overwriting the number.")
    phone_book[name] = number
    print("Ok!")

def quit():
    print("Quitting the program. Goodbye!")

def main_loop():
    while True:
        user_input = int(input("Command (1 search, 2 add, 3 quit): "))
        
        if user_input == 1:
            search_phone()

        elif user_input == 2:
            add_phone()

        elif user_input == 3:
            break

        else:
            print("Invalid input! Give 1 search, 2 add, 3 quit: ")

main_loop()