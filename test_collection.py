import unittest
from collection import Collection
from movie import Movie
from book import Book
from album import Album


class TestCollection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.movie = Movie()
        self.book = Book()
        self.album = Album()
        self.collection = Collection("Collection", [self.movie], [self.book], [self.album])

    def tearDown(self):
        pass

    def test_f__name(self):
        self.assertEqual(self.collection.f__name, "Collection")
        self.collection.f__name = "Collection 2"
        self.assertEqual(self.collection.f__name, "Collection 2")

    def test_f__movie_collection(self):
        self.assertEqual(self.collection.f__movie_collection, [self.movie])

    def test_f__book_collection(self):
        self.assertEqual(self.collection.f__book_collection, [self.book])

    def test_f__album_collection(self):
        self.assertEqual(self.collection.f__album_collection, [self.album])


if __name__ == '__main__':
    unittest.main()
