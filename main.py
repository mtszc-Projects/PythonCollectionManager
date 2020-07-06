from item import Item
from album import Album
from book import Book
from movie import Movie
from collection import Collection

new_item = Item()
new_item.display_data()
#new_item.write_data()
new_item.display_data()

new_album = Album()
new_album.display_data()

new_book = Book()
new_book.display_data()

new_movie = Movie()
new_movie.display_data()

new_collection = Collection()
print(new_collection.f__quantity())

