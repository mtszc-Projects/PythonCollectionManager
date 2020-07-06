from item import Item


class Movie(Item):
    def __init__(self, director="No data", script_writer="No data", length=0):
        super().__init__(item_type="Movie", title="No data", genre="No data", year=0, price=0)
        self.__director = director  # private attribute
        self.__script_writer = script_writer  # private attribute
        self.__length = length  # private attribute

    #  GETTERS
    @property
    def f__director(self):
        return self.__director

    @property
    def f__script_writer(self):
        return self.__script_writer

    @property
    def f__length(self):
        return self.__length

    #  SETTERS
    @f__director.setter
    def f__director(self, director):
        self.__director = director

    @f__script_writer.setter
    def f__script_writer(self, script_writer):
        self.__script_writer = script_writer

    @f__length.setter
    def f__length(self, length):
        self.__length = length

    def display_data(self):
        Item.display_data(self)
        print("Director: ", self.__director)
        print("Scriptwriter: ", self.__script_writer)
        print("Length: ", self.__length, " minutes")

    def write_data(self):
        Item.write_data(self)
        self.__director = input("Director: ")
        self.__script_writer = input("Scriptwriter: ")
        self.__length = input("Length: ")
        while type(self.__length) is not int:
            try:
                self.__length = int(self.__length)
            except ValueError:
                print("Length must be a number!")
                self.__length = input("Length: ")
