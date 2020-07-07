from item import Item


class Album(Item):
    def __init__(self, author="No data", length=0):
        super().__init__(item_type="Album", title="No data", genre="No data", year=0, price=0)
        self.__author = author  # private attribute
        self.__length = length  # private attribute

    #  GETTERS
    @property
    def f__author(self):
        return self.__author

    @property
    def f__length(self):
        return self.__length

    #  SETTERS
    @f__author.setter
    def f__author(self, author):
        self.__author = author

    @f__length.setter
    def f__length(self, length):
        self.__length = length

    def display_data(self):
        Item.display_data(self)
        print("Author: ", self.__author)
        print(f"Length: {self.__length}\n")

    def write_data(self):
        Item.write_data(self)
        self.__author = input("Author: ")
        self.__length = input("Length: ")
        while type(self.__length) is not int:
            try:
                self.__length = int(self.__length)
            except ValueError:
                print("Length must be a number!")
                self.__length = input("Length: ")
