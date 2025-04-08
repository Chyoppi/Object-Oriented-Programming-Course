"""
Refactor the code, in the exercise sheet there is a list of possible problems that you can find from this program. 
Some of the problems are overlapping, so you might fix two problems when you are fixing the code.

Hint. start by utilizing inheritance and method overriding, then continue with other parts of the code.

1. God Class:               Class Item from line 9-84
2. Shotgun Surgery:         Class Box from line 86-138
3. Speculative Generality:  -
4. Excessive Comments:      Class Item has bunch of comments which are not needed   
5. Inconsistent Naming:     -
6. Feature Envy:            Class Item and Box both have a method for infomation updating
7. Data Clumps:             Class PackItem has bunch of variables (Maybe can be made easier?)
8. Primitive Obsession:     -
9. Temporary Field:         -
10. Lazy Class:             -
11. Long Method:            Class PackItem has a long method for user interface
12. Duplicated Code:        Class Item and Box both have a method for infomation updating
13. Magic Numbers:          -
14. !!! No function for VIEW items !!!
"""
class Item:
    def __init__(self, title, year):
        self.__title = title
        self.__year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def description(self):
        return f"Title: {self.title}, Year: {self.year}"


class Book(Item):
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.__author = author

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    def description(self):
        return super().description() + f", Author: {self.author}"


class Music(Item):
    def __init__(self, title, artist, year):
        super().__init__(title, year)
        self.__artist = artist

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    def description(self):
        return super().description() + f", Artist: {self.artist}"


class Movie(Item):
    def __init__(self, title, director, year):
        super().__init__(title, year)
        self.__director = director

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, value):
        self.__director = value

    def description(self):
        return super().description() + f", Director: {self.director}"


class Game(Item):
    def __init__(self, title, developer, year):
        super().__init__(title, year)
        self.__developer = developer

    @property
    def developer(self):
        return self.__developer

    @developer.setter
    def developer(self, value):
        self.__developer = value

    def description(self):
        return super().description() + f", Developer: {self.developer}"

class Box:
    def __init__(self):
        self.items = {}

    def add_item(self, key, item: Item):
        self.items[key] = item

    def remove_item(self, key):
        if key in self.items:
            del self.items[key]
        else:
            print("No item found")

    def update_item(self, key, **kwargs):
        if key in self.items:
            self.items[key].update_info(**kwargs)
        else:
            print("No item found")

    def view_items(self):
        for item in self.items.values():
            print(item.description())


class PackItems:
    def __init__(self):
        self.box = Box()
        self.log = []

    def add_item_ui(self):
        title = input("Enter title: ")
        year = int(input("Enter year: "))
        item_type = input("Enter type (Book, Music, Movie, Game): ").lower()

        if item_type == "book":
            author = input("Enter author: ")
            item = Book(title, author, year)
        elif item_type == "music":
            artist = input("Enter artist: ")
            item = Music(title, artist, year)
        elif item_type == "movie":
            director = input("Enter director: ")
            item = Movie(title, director, year)
        elif item_type == "game":
            developer = input("Enter developer: ")
            item = Game(title, developer, year)
        else:
            print("Invalid type")
            return

        self.box.add_item(title, item)
        self.log.append(f"Added item: {title}")

    def remove_item_ui(self):
        title = input("Enter title of item to remove: ")
        self.box.remove_item(title)
        self.log.append(f"Removed item: {title}")

    def view_items_ui(self):
        print("\nItems in the box:")
        self.box.view_items()

    def user_interface(self):
        while True:
            print("\nOptions:")
            print("1. Add item")
            print("2. Remove item")
            print("3. View items")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_item_ui()
            elif choice == "2":
                self.remove_item_ui()
            elif choice == "3":
                self.view_items_ui()
            elif choice == "4":
                self.save_log()
                break
            else:
                print("Invalid option. Please try again.")

    def save_log(self):
        with open("log.txt", "w") as file:
            for entry in self.log:
                file.write(entry + "\n")

# Example usage:
"""
This is for testing the Item class
if __name__ == "__main__":
    item1 = Item(title="1984", author="George Orwell", year=1949)
item2 = Item(title="Thriller", artist="Michael Jackson", year=1982)
item3 = Item(title="Inception", director="Christopher Nolan", year=2010)
item4 = Item(title="The Legend of Zelda", developer="Nintendo", year=1986)

print(item1.print_item_description())
print(item2.print_item_description())
print(item3.print_item_description())
print(item4.print_item_description())"""

"""
This to for testing the Box class
if __name__ == "__main__":
    box = Box()
    box.add_item("1984", Item(title="1984", author="George Orwell", year=1949))
    box.add_item("Thriller", Item(title="Thriller", artist="Michael Jackson", year=1982))

    print("Before replacement:")
    for description in box.get_descriptions():
        print(description)

    box.replace_item("1984", "1984", Item(title="1984", author="George Orwell", year=1950))

    print("\nAfter replacement:")
    for description in box.get_descriptions():
        print(description)"""

if __name__ == "__main__":
    pack_items = PackItems()
    pack_items.user_interface()