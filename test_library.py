import pytest
from biblioteca import Book, User, Library
from biblioteca.exceptions import OutOfStockError, MaxBooksReachedError

def setup_library_with_book_and_users():
    lib = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien", 2)
    lib.add_book(book)
    lib.add_user(User("alice"))
    lib.add_user(User("bob"))
    lib.add_user(User("carol"))
    return lib

