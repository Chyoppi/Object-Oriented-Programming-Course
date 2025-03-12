class User:
    def __init__(self, name, age, userID):
        self.name = name
        self.age = age
        self.userID = userID

# Base class
class LibraryItem:
    def __init__(self, title, author, publication_year, itemID):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.itemID = itemID
        self.is_borrowed = False

    def return_item(self):
        self.is_borrowed = False
        print(f"{self.title} has been returned.")

    def borrow_item(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

# Sub-classes
class Book(LibraryItem):
    def __init__(self, title, author, publication_year, itemID, genre):
        super().__init__(title, author, publication_year, itemID)
        self.genre = genre

    def reading(self):
        print(f"{self.title} is being read.")

class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, itemID, issue):
        super().__init__(title, author, publication_year, itemID)
        self.issue = issue

    def reading(self):
        print(f"{self.title} is being read.")

class Newspaper(LibraryItem):
    def __init__(self, title, author, publication_year, itemID, issue):
        super().__init__(title, author, publication_year, itemID)
        self.issue = issue

    def reading(self):
        print(f"{self.title} is being read.")

class Manga(LibraryItem):
    def __init__(self, title, author, publication_year, itemID, issue):
        super().__init__(title, author, publication_year, itemID)
        self.issue = issue

    def reading(self):
        print(f"{self.title} is being read.")

class Comic(LibraryItem):
    def __init__(self, title, author, publication_year, itemID, issue):
        super().__init__(title, author, publication_year, itemID)
        self.issue = issue

    def reading(self):
        print(f"{self.title} is being read.")

class Audiobook(LibraryItem):
    def __init__(self, title, author, publication_year, itemID, duration):
        super().__init__(title, author, publication_year, itemID)
        self.duration = duration

    def listening(self):
        print(f"{self.title} is being listened to.")

#Main library catalog class
class LibraryCatalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: LibraryItem):
        self.items.append(item)
        print(f"{item.title} has been added to the catalog.")

    def remove_item(self, itemID: str):
        self.items = [item for item in self.items if item.itemID != itemID]
        print(f"Item with ID {itemID} has been removed from the catalog.")

    def search_item(self, title: str):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None

    def borrow_item(self, itemID: str):
        item = self.search_item_by_id(itemID)
        if item:
            item.borrow_item()
        else:
            print(f"Item with ID {itemID} not found in the catalog.")

    def return_item(self, itemID: str):
        item = self.search_item_by_id(itemID)
        if item:
            item.return_item()
        else:
            print(f"Item with ID {itemID} not found in the catalog.")

    def search_item_by_id(self, itemID: str):
        for item in self.items:
            if item.itemID == itemID:
                return item
        return None

# Example usage
catalog = LibraryCatalog()

book = Book("Destroying Arasaka", "Silverhand", 2077, "B001", "Cyberpunk")
magazine = Magazine("National Geographic", "Various", 2021, "M001", "March 2021")
newspaper = Newspaper("The New York Times", "Various", 2021, "N001", "April 2021")
manga = Manga("Naruto", "Masashi Kishimoto", 1999, "MG001", "Volume 1")
comic = Comic("Spider-Man", "Stan Lee", 1962, "C001", "Issue 1")
audiobook = Audiobook("Rebel Path", "V", 1949, "A001", "11 hours")

catalog.add_item(book)
catalog.add_item(magazine)
catalog.add_item(newspaper)
catalog.add_item(manga)
catalog.add_item(comic)
catalog.add_item(audiobook)

catalog.borrow_item("B001")
catalog.return_item("B001")
catalog.remove_item("M001")

"""
Borrowing an Item
User -> Library System: Search for an item
System -> Database: Fetch matching items
System -> User: Display search results
User -> System: Select an item to borrow
System -> Database: Check availability
If Available: System marks item as Borrowed
If Not Available: System informs user

2. Returning an Item
User -> Library System: Return item
System -> Database: Update item status to Available
"""