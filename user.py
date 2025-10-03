from typing import List
from .exceptions import MaxBooksReachedError

MAX_BORROW = 3

class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowed: List[str] = []

    def borrow(self, book_title: str):
        if len(self.borrowed) >= MAX_BORROW:
            raise MaxBooksReachedError(f"user '{self.name}' cannot borrow more than {MAX_BORROW} books")
        self.borrowed.append(book_title)

    def return_book(self, book_title: str):
        if book_title not in self.borrowed:
            raise ValueError(f"user '{self.name}' does not have book '{book_title}' borrowed")
        self.borrowed.remove(book_title)
