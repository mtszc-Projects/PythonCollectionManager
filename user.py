class User:

    __quantity = 2  # max no of each type of item in collection
    __max_collections = 3  # max different collection for one user

    def __init__(self, name="Unknown", surname="User", user_collection=None):
        self.__name = name  # private attribute
        self.__surname = surname  # private attribute
        self.__user_collection = user_collection if user_collection else []  # private attribute

    # GETTERS

    @classmethod
    def f__quantity(cls):
        return cls.__quantity

    @classmethod
    def f__max_collections(cls):
        return cls.__max_collections

    @property
    def f__name(self):
        return self.__name

    @property
    def f__surname(self):
        return self.__surname

    @property
    def f__user_collection(self):
        return self.__user_collection

    #  SETTERS

    @f__name.setter
    def f__name(self, name):
        self.__name = name

    @f__surname.setter
    def f__surname(self, surname):
        self.__surname = surname
