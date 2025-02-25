class Recording:
    def __init__(self, length: int):
        self.__length = length  # Private variable

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: int):
        self.__length = new_length

# Example usage
the_wall = Recording(43)
print(the_wall.length)  # Output: 43
the_wall.length = 44
print(the_wall.length)  # Output: 44