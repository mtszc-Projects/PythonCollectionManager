import unittest
from item import Item
from movie import Movie
from book import Book
from album import Album


class TestItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.item = Item("Item", "Car", "Action", 1999, 18)
        self.movie = Movie("Tarantino", "Tarantino", 180)
        self.book = Book("Adam Mickiewicz", 320)
        self.album = Album("Tymanski", 46)

    def tearDown(self):
        pass

# Functions from Item class

    def test_f__item_type(self):
        # ITEM
        self.assertEqual(self.item.f__item_type, 'Item')
        self.item.f__item_type = "Item 2"
        self.assertEqual(self.item.f__item_type, 'Item 2')
        # MOVIE
        self.assertEqual(self.movie.f__item_type, 'Movie')
        self.movie.f__item_type = "Movie 2"
        self.assertEqual(self.movie.f__item_type, 'Movie 2')
        # BOOK
        self.assertEqual(self.book.f__item_type, 'Book')
        self.book.f__item_type = "Book 2"
        self.assertEqual(self.book.f__item_type, 'Book 2')
        # ALBUM
        self.assertEqual(self.album.f__item_type, 'Album')
        self.album.f__item_type = "Album 2"
        self.assertEqual(self.album.f__item_type, 'Album 2')

    def test_f__title(self):
        # ITEM
        self.assertEqual(self.item.f__title, 'Car')
        self.item.f__title = "Car 2"
        self.assertEqual(self.item.f__title, 'Car 2')
        # MOVIE
        self.assertEqual(self.movie.f__title, 'No data')
        self.movie.f__title = "No data 2"
        self.assertEqual(self.movie.f__title, 'No data 2')
        # BOOK
        self.assertEqual(self.book.f__title, 'No data')
        self.book.f__title = "No data 2"
        self.assertEqual(self.book.f__title, 'No data 2')
        # ALBUM
        self.assertEqual(self.album.f__title, 'No data')
        self.album.f__title = "No data 2"
        self.assertEqual(self.album.f__title, 'No data 2')

    def test_f__genre(self):
        # ITEM
        self.assertEqual(self.item.f__genre, 'Action')
        self.item.f__genre = "Action 2"
        self.assertEqual(self.item.f__genre, 'Action 2')
        # MOVIE
        self.assertEqual(self.movie.f__genre, 'No data')
        self.movie.f__genre = "No data 2"
        self.assertEqual(self.movie.f__genre, 'No data 2')
        # BOOK
        self.assertEqual(self.book.f__genre, 'No data')
        self.book.f__genre = "No data 2"
        self.assertEqual(self.book.f__genre, 'No data 2')
        # ALBUM
        self.assertEqual(self.album.f__genre, 'No data')
        self.album.f__genre = "No data 2"
        self.assertEqual(self.album.f__genre, 'No data 2')

    def test_f__year(self):
        # ITEM
        self.assertEqual(self.item.f__year, 1999)
        self.item.f__year = 2000
        self.assertEqual(self.item.f__year, 2000)
        # MOVIE
        self.assertEqual(self.movie.f__year, 0)
        self.movie.f__year = 1
        self.assertEqual(self.movie.f__year, 1)
        # BOOK
        self.assertEqual(self.book.f__year, 0)
        self.book.f__year = 1
        self.assertEqual(self.book.f__year, 1)
        # ALBUM
        self.assertEqual(self.album.f__year, 0)
        self.album.f__year = 1
        self.assertEqual(self.album.f__year, 1)

    def test_f__price(self):
        # ITEM
        self.assertEqual(self.item.f__price, 18)
        self.item.f__price = 19
        self.assertEqual(self.item.f__price, 19)
        # MOVIE
        self.assertEqual(self.movie.f__price, 0)
        self.movie.f__price = 1
        self.assertEqual(self.movie.f__price, 1)
        # BOOK
        self.assertEqual(self.book.f__price, 0)
        self.book.f__price = 1
        self.assertEqual(self.book.f__price, 1)
        # ALBUM
        self.assertEqual(self.album.f__price, 0)
        self.album.f__price = 1
        self.assertEqual(self.album.f__price, 1)

# Function from Movie and Album class

    def test_f__length(self):
        # MOVIE
        self.assertEqual(self.movie.f__length, 180)
        self.movie.f__length = 181
        self.assertEqual(self.movie.f__length, 181)
        # ALBUM
        self.assertEqual(self.album.f__length, 46)
        self.album.f__length = 47
        self.assertEqual(self.album.f__length, 47)

# Function from Book and Album class

    def test_f__author(self):
        # BOOK
        self.assertEqual(self.book.f__author, 'Adam Mickiewicz')
        self.book.f__author = 'Adam Mickiewicz 2'
        self.assertEqual(self.book.f__author, 'Adam Mickiewicz 2')
        # ALBUM
        self.assertEqual(self.album.f__author, 'Tymanski')
        self.album.f__author = 'Tymanski 2'
        self.assertEqual(self.album.f__author, 'Tymanski 2')

# Functions from Movie class only

    def test_f__director(self):
        self.assertEqual(self.movie.f__director, 'Tarantino')
        self.movie.f__director = 'Tarantino 2'
        self.assertEqual(self.movie.f__director, 'Tarantino 2')

    def test_f__script_writer(self):
        self.assertEqual(self.movie.f__script_writer, 'Tarantino')
        self.movie.f__script_writer = "Tarantino 2"
        self.assertEqual(self.movie.f__script_writer, 'Tarantino 2')

# Functions from Book class only

    def test_f__pages(self):
        self.assertEqual(self.book.f__pages, 320)
        self.book.f__pages = 'qwe'
        self.assertEqual(self.book.f__pages, 'qwe')


if __name__ == '__main__':
    unittest.main()
