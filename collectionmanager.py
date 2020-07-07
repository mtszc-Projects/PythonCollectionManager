from os import system, name
from collection import Collection
from book import Book
from movie import Movie
from album import Album


class CollectionManager:

    def __init__(self, user):
        self.__user = user  # private attribute

    @staticmethod
    def clear():
        system('cls' if name == 'nt' else 'clear')

    def switch(self, arg):
        switcher = {
            1: self.add_collection,
            2: self.add_item,
            3: self.display_collection,
            4: self.display_category,
            5: self.change_collection_name,
            6: self.search_item,
            7: self.update_item,
            8: self.statistics,
            9: self.delete_item,
            10: self.delete_collection,
            11: self.save_to_file,
            12: exit
        }
        switcher.get(arg)()

    def name_change(self):
        flag = input(f"Hello {self.__user.f__name} {self.__user.f__surname}! Do you want to change your name? (y/n)\n")
        if flag == "y":
            new_name = input("Provide your name: ")
            new_surname = input("Provide your surname: ")
            self.__user.f__name = new_name
            self.__user.f__surname = new_surname

    def collection_not_created(self):
        input("To do this action you have to create collection first.\n\n"
              "Press ENTER to go back to main menu: ")
        self.clear()

    def exit_to_menu(self):
        input("Press ENTER to go back to main menu: ")
        self.clear()

    def add_collection(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length >= self.__user.f__max_collections():
            print("You can't create new collection, you already reached maximum number of collections."
                  "You can modify existing collections or delete one of them.")
            self.exit_to_menu()
        else:
            collection_name = input(f"How you want to name collection no {length+1}?: ")
            new_collection = Collection()
            self.__user.f__user_collection.append(new_collection)
            self.__user.f__user_collection[length].f__name = collection_name
            print(f"\nCongratulations! You created new collection named: "
                  f"{self.__user.f__user_collection[length-1].f__name}\n")
            self.exit_to_menu()

    def add_item(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length == 0:
            self.collection_not_created()
        else:
            print("To which collection you want to add item?")
            for _ in range(length):
                print(f"{_+1}: {self.__user.f__user_collection[_].f__name}")
            flag = input("Choose the number from list above: ")
            while type(flag) is not int:
                try:
                    flag = int(flag)
                    if flag <= 0 or flag > length:
                        flag = input("Choose the number from list above: ")
                except ValueError:
                    flag = input("Choose the number from list above: ")
            collection = self.__user.f__user_collection[flag-1]
            item_type = input(f"What you want to add to collection {collection.f__name}?\n"
                              f"(book - press b; movie - press m; album - press a):")
            while item_type != 'b' and item_type != 'm' and item_type != 'a':
                item_type = input(
                    f"What you want to add to collection {collection.f__name}?\n"
                    f"(book - press b; movie - press m; album - press a):")
            if item_type == 'b':
                if len(collection.f__book_collection) < self.__user.f__max_collections():
                    new_book = Book()
                    new_book.write_data()
                    collection.f__book_collection.append(new_book)
                else:
                    print("You can't add new book. You have maximum amount of books in that collection.\n"
                          "If you want you can modify or delete existing books.\n")
                    self.exit_to_menu()
            elif item_type == 'm':
                if len(collection.f__movie_collection) < self.__user.f__max_collections():
                    new_movie = Movie()
                    new_movie.write_data()
                    collection.f__movie_collection.append(new_movie)
                else:
                    print("You can't add new movie. You have maximum amount of movies in that collection.\n"
                          "If you want you can modify or delete existing movies.\n")
                    self.exit_to_menu()
            else:
                if len(collection.f__album_collection) < self.__user.f__max_collections():
                    new_album = Album()
                    new_album.write_data()
                    collection.f__album_collection.append(new_album)
                else:
                    print("You can't add new album. You have maximum amount of albums in that collection.\n"
                          "If you want you can modify or delete existing albums.\n")
                    self.exit_to_menu()
            print(f"Item successfully added to your collection {collection.f__name}\n"
                  f"At the moment in this collection you have: "
                  f"{len(collection.f__book_collection)} books, "
                  f"{len(collection.f__movie_collection)} movies and "
                  f"{len(collection.f__album_collection)} albums.")
            self.exit_to_menu()

    def display_collection(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length == 0:
            self.collection_not_created()
        else:
            print("Which collection you want to display?")
            for _ in range(length):
                print(f"{_ + 1}: {self.__user.f__user_collection[_].f__name}")
            flag = input("Choose the number from list above: ")
            while type(flag) is not int:
                try:
                    flag = int(flag)
                    if flag <= 0 or flag > len(self.__user.f__user_collection):
                        flag = input("Choose the number from list above: ")
                except ValueError:
                    flag = input("Choose the number from list above: ")
            collection = self.__user.f__user_collection[flag - 1]
            self.clear()
            print(f"Collection {collection.f__name} content: \n")
            print("BOOKS:\n")
            for book in collection.f__book_collection:
                book.display_data()
            print("MOVIES:\n")
            for movie in collection.f__movie_collection:
                movie.display_data()
            print("ALBUMS:\n")
            for album in collection.f__album_collection:
                album.display_data()
            self.exit_to_menu()

    def display_category(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length == 0:
            self.collection_not_created()
        else:
            item_type = input(f"Which category you want to display?\n"
                              f"(book - press b; movie - press m; album - press a):")
            while item_type != 'b' and item_type != 'm' and item_type != 'a':
                item_type = input(f"Which category you want to display?\n"
                                  f"(book - press b; movie - press m; album - press a):")
            counter = 0
            if item_type == 'b':
                print("\nAll books in all collections: \n")
                for collection in self.__user.f__user_collection:
                    for book in collection.f__book_collection:
                        if len(collection.f__book_collection) > 0:
                            print(f"Collection: {collection.f__name}")
                            book.display_data()
                            counter += 1
                if counter == 0:
                    print("In your collections there isn't any books.")
            if item_type == 'm':
                print("\nAll movies in all collections: \n")
                for collection in self.__user.f__user_collection:
                    for movie in collection.f__movie_collection:
                        if len(collection.f__movie_collection) > 0:
                            print(f"Collection: {collection.f__name}:")
                            movie.display_data()
                            counter += 1
                if counter == 0:
                    print("In your collections there isn't any movies.")
            if item_type == 'a':
                print("\nAll albums in all collections: \n")
                for collection in self.__user.f__user_collection:
                    for album in collection.f__album_collection:
                        if len(collection.f__album_collection) > 0:
                            print(f"Collection: {collection.f__name}:")
                            album.display_data()
                            counter += 1
                if counter == 0:
                    print("In your collections there isn't any albums.")
            self.exit_to_menu()

    def change_collection_name(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length == 0:
            self.collection_not_created()
        else:
            print("Which collection you want to rename?")
            for _ in range(length):
                print(f"{_+1}: {self.__user.f__user_collection[_].f__name}")
            flag = input("Choose the number from list above: ")
            while type(flag) is not int:
                try:
                    flag = int(flag)
                    if flag <= 0 or flag > len(self.__user.f__user_collection):
                        flag = input("Choose the number from list above: ")
                except ValueError:
                    flag = input("Choose the number from list above: ")
            collection = self.__user.f__user_collection[flag-1]
            new_name = input(f"What's the new name for collection {collection.f__name}?:")
            collection.f__name = new_name
            print(f"You successfully changed name of collection. New name is: {collection.f__name}")
            self.exit_to_menu()

    def search_item(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length == 0:
            self.collection_not_created()
        else:
            search_name = input("Type in phrase you looking for: ")
            counter = 0
            print("Items with provided phrase in title: \n")
            for collection in self.__user.f__user_collection:
                if len(collection.f__book_collection) > 0:
                    for book in collection.f__book_collection:
                        if search_name in book.f__title:
                            print(f"Collection: {collection.f__name}")
                            book.display_data()
                            counter += 1
                if len(collection.f__movie_collection) > 0:
                    for movie in collection.f__movie_collection:
                        if search_name in movie.f__title:
                            print(f"Collection: {collection.f__name}")
                            movie.display_data()
                            counter += 1
                if len(collection.f__album_collection) > 0:
                    for album in collection.f__album_collection:
                        if search_name in album.f__title:
                            print(f"Collection: {collection.f__name}")
                            album.display_data()
                            counter += 1
            if counter == 0:
                print("In your collections there is no item with provided phrase in title.")
            self.exit_to_menu()

    def update_item(self):
        self.clear()
        length = len(self.__user.f__user_collection)
        if length == 0:
            self.collection_not_created()
        else:
            print("In which collection you want to update item?")
            for _ in range(len(self.__user.f__user_collection)):
                print(f"{_ + 1}: {self.__user.f__user_collection[_].f__name}")
            flag = input("Choose the number from list above: ")
            while type(flag) is not int:
                try:
                    flag = int(flag)
                    if flag <= 0 or flag > len(self.__user.f__user_collection):
                        flag = input("Choose the number from list above: ")
                except ValueError:
                    flag = input("Choose the number from list above: ")
            collection = self.__user.f__user_collection[flag-1]
            item_type = input(f"Which type of item you want to update?\n"
                              f"(book - press b; movie - press m; album - press a):")
            while item_type != 'b' and item_type != 'm' and item_type != 'a':
                item_type = input(f"Which type of item you want to update?\n"
                                  f"(book - press b; movie - press m; album - press a):")
            if item_type == 'b':
                print("\nBOOKS: \n")
                if len(collection.f__book_collection) > 0:
                    counter = 1
                    for book in collection.f__book_collection:
                        print(f"Book no: {counter}")
                        book.display_data()
                        counter += 1
                    book_number = input("Choose the book number from list above: ")
                    while type(book_number) is not int:
                        try:
                            book_number = int(book_number)
                            if book_number <= 0 or book_number > len(collection.f__book_collection):
                                book_number = input("Choose the book number from list above: ")
                        except ValueError:
                            book_number = input("Choose the book number from list above: ")
                    collection.f__book_collection[book_number-1].write_data()
                    print("Item updated successfully!")
                else:
                    print("In this collection there isn't any books.")
            elif item_type == 'm':
                print("\nMOVIES: \n")
                if len(collection.f__movie_collection) > 0:
                    counter = 1
                    for movie in collection.f__movie_collection:
                        print(f"Movie no: {counter}")
                        movie.display_data()
                        counter += 1
                    movie_number = input("Choose the movie number from list above: ")
                    while type(movie_number) is not int:
                        try:
                            movie_number = int(movie_number)
                            if movie_number <= 0 or movie_number > len(collection.f__movie_collection):
                                movie_number = input("Choose the movie number from list above: ")
                        except ValueError:
                            movie_number = input("Choose the movie number from list above: ")
                    collection.f__movie_collection[movie_number - 1].write_data()
                    print("Item updated successfully!")
                else:
                    print("In this collection there isn't any movies.")
            elif item_type == 'a':
                print("\nALBUMS: \n")
                if len(collection.f__album_collection) > 0:
                    counter = 1
                    for album in collection.f__album_collection:
                        print(f"Album no: {counter}")
                        album.display_data()
                        counter += 1
                    album_number = input("Choose the album number from list above: ")
                    while type(album_number) is not int:
                        try:
                            album_number = int(album_number)
                            if album_number <= 0 or album_number > len(collection.f__album_collection):
                                album_number = input("Choose the album number from list above: ")
                        except ValueError:
                            album_number = input("Choose the album number from list above: ")
                    collection.f__album_collection[album_number - 1].write_data()
                    print("Item updated successfully!")
                else:
                    print("In this collection there isn't any movies.")
            self.exit_to_menu()

    def statistics(self):
        pass

    def delete_item(self):
        pass

    def delete_collection(self):
        pass

    def save_to_file(self):
        pass

    def manage(self):
        self.clear()
        self.name_change()
        choice = 0
        while choice != 12:
            print(f"{self.__user.f__name} you can create {self.__user.f__quantity()} different collections,"
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
                    if choice < 1 or choice > 12:
                        self.clear()
                    else:
                        self.switch(choice)
                except ValueError:
                    self.clear()
                    break
