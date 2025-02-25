class  NumberStats:
    def __init__(self):
        #no need to add any new varibales here, just change the
        #initialization of the self.numbers variable.
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        return self.get_sum() / self.count_numbers()

if __name__ == "__main__":
    """ #Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers()) """

    """ #Part 2 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average()) """

    #Part 3 test prints:
    stats = NumberStats()

    while True:
        number = int(input("Please type in integer numbers: "))
        if number != -1:
            stats.add_number(number)
        else:
            break
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())

    # Part 4 test prints:
    stats_all = NumberStats()
    stats_even = NumberStats()
    stats_odd = NumberStats()

    while True:
        number = int(input("Please type in integer numbers: "))
        if number != -1:
            stats_all.add_number(number)
            if number % 2 == 0:
                stats_even.add_number(number)
            else:
                stats_odd.add_number(number)
        else:
            break

    print("Sum of numbers:", stats_all.get_sum())
    print("Mean of numbers:", stats_all.average())
    print("Sum of even numbers:", stats_even.get_sum())
    print("Sum of odd numbers:", stats_odd.get_sum())
