#The program contains the class definition City , which is a model of a single city.
#Please add a class variable named postcodes which refers to a dictionary. 
#The keys of the dictionary are the names of cities, and the values attached are the postcodes for those cities. Both are strings.

#The dictionary should contain at least the following postcodes:
# •Helsinki 00100
# •Turku 20100
# •Tampere 33100
# •Salo 24100
# •Oulu 90100
# •Jyväskylä 40100

#You do not need to implement any other functionality for the class.

class City:

    postcodes = {"Helsinki": "00100", "Turku": "20100", "Tampere": "33100", "Salo": "24100", "Oulu": "90100", "Jyväskylä": "40100"}

    def __init__(self, nimi:str, population:int,):
        self.__nimi = nimi
        self.__population = population