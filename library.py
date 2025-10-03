from collections import deque
from typing import Dict
from .book import Book
from .user import User
from .exceptions import OutOfStockError, MaxBooksReachedError

class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.reservations: Dict[str, deque] = {}

    def add_book(self, book: Book):
        if book.title in self.books:
            existing = self.books[book.title]
            existing.increase_stock(book.quantity)
        else:
            self.books[book.title] = Book(book.title, book.author, book.quantity)
        if book.title not in self.reservations:
            self.reservations[book.title] = deque()

    def add_user(self, user: User):
        if user.name not in self.users:
            self.users[user.name] = user

    def reserve_book(self, title: str, username: str):
        if title not in self.books:
            raise ValueError("book not found")
        if username not in self.users:
            raise ValueError("user not found")
        q = self.reservations.setdefault(title, deque())
        if username not in q:
            q.append(username)

    def lend_book(self, title: str, username: str):
        if title not in self.books:
            raise ValueError("book not found")
        if username not in self.users:
            raise ValueError("user not found")

        user = self.users[username]
        book = self.books[title]

        if len(user.borrowed) >= 3:
            raise MaxBooksReachedError(f"user '{username}' has reached the maximum number of borrowed books")

        if book.quantity <= 0:
            raise OutOfStockError(f"book '{title}' is out of stock")

        book.decrease_stock(1)
        user.borrow(title)

    def return_book(self, title: str, username: str):
        if title not in self.books:
            raise ValueError("book not found")
        if username not in self.users:
            raise ValueError("user not found")

        user = self.users[username]
        book = self.books[title]

        user.return_book(title)
        book.increase_stock(1)

        q = self.reservations.get(title)
        if not q:
            return

        while q and book.quantity > 0:
            next_username = q.popleft()
            reserver = self.users.get(next_username)
            if reserver is None:
                continue
            if len(reserver.borrowed) >= 3:
                continue
            try:
                book.decrease_stock(1)
                reserver.borrow(title)
            except Exception:
                continue
