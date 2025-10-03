import pytest
from biblioteca.book import Book

def test_create_valid_book():
    b = Book("1984", "George Orwell", 5)
    assert b.title == "1984"
    assert b.author == "George Orwell"
    assert b.quantity == 5

def test_negative_stock_not_allowed():
    with pytest.raises(ValueError):
        Book("Bad Book", "Author", -1)

def test_increase_and_decrease_stock_success():
    b = Book("Dune", "Frank Herbert", 3)
    b.increase_stock(2)
    assert b.quantity == 5
    b.decrease_stock(3)
    assert b.quantity == 2

def test_decrease_more_than_available_raises():
    b = Book("Clean Code", "Robert C. Martin", 1)
    with pytest.raises(ValueError):
        b.decrease_stock(2)
