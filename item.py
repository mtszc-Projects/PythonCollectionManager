class Item:
    def __init__(self, item_type="No data", title="No data", genre="No data", year=0, price=0):
        self.__item_type = item_type  # private attribute
        self.__title = title  # private attribute
        self.__genre = genre  # private attribute
        self.__year = year  # private attribute
        self.__price = price  # private attribute

    #  GETTERS
    @property
    def f__item_type(self):
        return self.__item_type

    @property
    def f__title(self):
        return self.__title

    @property
    def f__genre(self):
        return self.__genre

    @property
    def f__year(self):
        return self.__year

    @property
    def f__price(self):
        return self.__price

    #  SETTERS
    @f__item_type.setter
    def f__item_type(self, item_type):
        self.__item_type = item_type

    @f__title.setter
    def f__title(self, title):
        self.__title = title

    @f__genre.setter
    def f__genre(self, genre):
        self.__genre = genre

    @f__year.setter
    def f__year(self, year):
        self.__year = year

    @f__price.setter
    def f__price(self, price):
        self.__price = price

    def display_data(self):
        print("Type: ", self.__item_type)
        print("Title: ", self.__title)
        print("Genre: ", self.__genre)
        print("Year: ", self.__year)
        print("Price: ", self.__price, "$")

    def write_data(self):
        self.__title = input("Title: ")
        self.__genre = input("Genre: ")
        self.__year = input("Year: ")
        while type(self.__year) is not int:
            try:
                self.__year = int(self.__year)
            except ValueError:
                print("Year must be a number!")
                self.__year = input("Year: ")
        self.__price = input("Price: ")
        while type(self.__price) is not int:
            try:
                self.__price = int(self.__price)
            except ValueError:
                print("Price must be a number!")
                self.__price = input("Price: ")
