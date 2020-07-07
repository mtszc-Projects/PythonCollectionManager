from item import Item


class Book(Item):
    def __init__(self, author="No data", pages=0):
        super().__init__(item_type="Book", title="No data", genre="No data", year=0, price=0)
        self.__author = author  # private attribute
        self.__pages = pages  # private attribute

    #  GETTERS
    @property
    def f__author(self):
        return self.__author

    @property
    def f__pages(self):
        return self.__pages

    #  SETTERS
    @f__author.setter
    def f__author(self, author):
        self.__author = author

    @f__pages.setter
    def f__pages(self, pages):
        self.__pages = pages

    def display_data(self):
        Item.display_data(self)
        print("Author: ", self.__author)
        print(f"Pages: {self.__pages}\n")

    def write_data(self):
        Item.write_data(self)
        self.__author = input("Author: ")
        self.__pages = input("Pages: ")
        while type(self.__pages) is not int:
            try:
                self.__pages = int(self.__pages)
            except ValueError:
                print("Pages must be a number!")
                self.__pages = input("Pages: ")
