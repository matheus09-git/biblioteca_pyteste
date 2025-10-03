import pytest
from biblioteca.user import User
from biblioteca.exceptions import MaxBooksReachedError

def test_create_user():
    u = User("Alice")
    assert u.name == "Alice"
    assert u.borrowed == []

