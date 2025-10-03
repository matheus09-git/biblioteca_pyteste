from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    quantity: int

    def __post_init__(self):
        if not isinstance(self.quantity, int):
            raise TypeError("quantity must be an integer")
        if self.quantity < 0:
            raise ValueError("quantity cannot be negative")

    def increase_stock(self, n: int = 1):
        if n < 0:
            raise ValueError("increase amount must be non-negative")
        self.quantity += n

    def decrease_stock(self, n: int = 1):
        if n < 0:
            raise ValueError("decrease amount must be non-negative")
        if n > self.quantity:
            raise ValueError("cannot decrease more than available stock")
        self.quantity -= n
