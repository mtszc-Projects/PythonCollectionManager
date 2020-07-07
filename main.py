from user import User
from collectionmanager import CollectionManager


def main():
    user = User()
    manager1 = CollectionManager(user)
    manager1.manage()


main()
