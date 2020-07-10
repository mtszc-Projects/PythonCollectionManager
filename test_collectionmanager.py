import unittest
from collectionmanager import CollectionManager
from user import User


class TestCollectionManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.user = User("Mateusz", "Cieciura")
        self.collectionmanager = CollectionManager(self.user)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
