import unittest
from user import User
from collection import Collection


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.collection = Collection()
        self.user = User("Unknown", "User", [self.collection])

    def tearDown(self):
        pass

    def test_f__name(self):
        self.assertEqual(self.user.f__name, "Unknown")
        self.user.f__name = "Unknown 2"
        self.assertEqual(self.user.f__name, "Unknown 2")

    def test_f__surname(self):
        self.assertEqual(self.user.f__surname, "User")
        self.user.f__surname = "User 2"
        self.assertEqual(self.user.f__surname, "User 2")

    def test_f__user_collection(self):
        self.assertEqual(self.user.f__user_collection, [self.collection])


if __name__ == '__main__':
    unittest.main()
