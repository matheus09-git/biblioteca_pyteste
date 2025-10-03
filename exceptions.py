class LibraryError(Exception):
    pass

class OutOfStockError(LibraryError):
    pass

class MaxBooksReachedError(LibraryError):
    pass
