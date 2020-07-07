from os import system, name
from collection import Collection


class CollectionManager:

    def __init__(self, user):
        self.__user = user  # private attribute

    @staticmethod
    def clear():
        _ = system('cls' if name == 'nt' else 'clear')

    def switch(self, arg):
        switcher = {
            1: self.add_collection(),
            2: self.add_item(),
            3: self.display_collection(),
            4: self.display_category(),
            5: self.change_collection_name(),
            6: self.search_item(),
            7: self.update_item(),
            8: self.statistics(),
            9: self.delete_item(),
            10: self.delete_collection(),
            11: self.save_to_file(),
            12: exit()
        }
        switcher.get(arg)

    def name_change(self):
        flag = input(f"Hello {self.__user.f__name} {self.__user.f__surname}! Do you want to change your name? (y/n)")
        if flag == "y":
            new_name = input("Provide your name: ")
            new_surname = input("Provide your surname: ")
            self.__user.f__name = new_name
            self.__user.f__surname = new_surname

    def collection_not_created(self):
        pass

    def exit_to_menu(self):
        input("Press enter to go back to main menu: ")
        self.clear()
        self.manage()

    def add_collection(self):
        self.clear()
        if len(self.__user.f__user_collection) >= self.__user.f__max_collections():
            print("You can't create new collection, you already reached maximum number of collections."
                  "You can modify existing collections or delete one of them.")
            self.exit_to_menu()
        else:
            collection_name = input(f"How you want to name collection no {len(self.__user.f__user_collection)+1}?: ")
            new_collection = Collection()
            self.__user.f__user_collection.append(new_collection)
            self.__user.f__user_collection[len(self.__user.f__user_collection)-1].f__name = collection_name
            print(f"\nCongratulations! You created new collection: "
                  f"{self.__user.f__user_collection[len(self.__user.f__user_collection)-1].f__name}\n")
            self.exit_to_menu()

    def add_item(self):
        pass

    def display_collection(self):
        pass

    def display_category(self):
        pass

    def change_collection_name(self):
        pass

    def search_item(self):
        pass

    def update_item(self):
        pass

    def statistics(self):
        pass

    def delete_item(self):
        pass

    def delete_collection(self):
        pass

    def save_to_file(self):
        pass

    def manage(self):
        # self.name_change()
        choice = 0
        while choice != 12:
            print(f"\n{self.__user.f__name} you can create {self.__user.f__quantity()} different collections,"
                  f" which can represent vary \ncategories (i.e. happy, sad, etc.) In all of them you can save"
                  f" your favourites \nbooks, movies and music albums. At max you could save"
                  f" {self.__user.f__max_collections()} of each item in every collection.\n")

            print(f"{self.__user.f__name} {self.__user.f__surname} currently you have"
                  f" {len(self.__user.f__user_collection)} collections:")

            for _ in self.__user.f__user_collection:
                print(f"- {_.f__name}")

            print("\nYou can choose actions from below list:\n")
            print("1.  Create new collection.                           (press:  1)")
            print("2.  Add item to already created collection.          (press:  2)")
            print("3.  Display content of chosen collection.            (press:  3)")
            print("4.  Display content of chosen category.              (press:  4)")
            print("5.  Change name of chosen collection.                (press:  5)")
            print("6.  Search item in collections.                      (press:  6)")
            print("7.  Modify item in collection.                       (press:  7)")
            print("8.  Display statistics of items.                     (press:  8)")
            print("9.  Delete item from collection                      (press:  9)")
            print("10. Delete collection.                               (press: 10)")
            print("11. Save collections to file.                        (press: 11)")
            print("12. Exit program.                                    (press: 12)\n")

            choice = input("Choose the number from above list: ")
            while type(choice) is not int:
                try:
                    choice = int(choice)
                except ValueError:
                    choice = input("Choose the number from above list: ")
            if choice < 1 or choice > 12:
                self.clear()
            else:
                self.switch(choice)
