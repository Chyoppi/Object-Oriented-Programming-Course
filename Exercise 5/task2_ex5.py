numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5] 

class ListHelper:
    def __init__(self, list_number:list):
        self.list_number = list_number

    def greatest_frequency(self):
        most_frequent = {}
        for value in self.list_number:
            if value in most_frequent:
                most_frequent[value] += 1
            else:
                most_frequent[value] = 1
        
        #Returns the key with the highest value
        return max(most_frequent, key=most_frequent.get)
    
    def doubles(self):
        number_dict = {}
        for value in self.list_number:
            if value in number_dict:
                number_dict[value] += 1
            else:
                number_dict[value] = 1
            #Sums every value in dictionary that is greater than 1
        unique_doubles = sum(1 for count in number_dict.values() if count > 1)
        return unique_doubles
    

print(ListHelper(numbers).greatest_frequency()) 
print(ListHelper(numbers).doubles())

