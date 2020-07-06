class Collection:

    __quantity = 2  # max no of each type of item in collection

    def __init__(self, name="No data", movie_collection=None, book_collection=None, album_collection=None):

        self.__name = name  # private attribute
        self.__movie_collection = movie_collection if movie_collection else []  # private attribute
        self.__book_collection = book_collection if book_collection else []  # private attribute
        self.__album_collection = album_collection if album_collection else []  # private attribute

    #  GETTERS
    @classmethod
    def f__quantity(cls):
        return cls.__quantity

    @property
    def f__name(self):
        return self.__name

    @property
    def f__movie_collection(self):
        return self.__movie_collection

    @property
    def f__book_collection(self):
        return self.__book_collection

    @property
    def f__album_collection(self):
        return self.__album_collection

    #  SETTERS

    @f__name.setter
    def f__name(self, name):
        self.__name = name
