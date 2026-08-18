from .base_book import Book


class PaperBook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn, is_rented)
        self.__pages = pages


class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn, is_rented)
        self.__file_size = file_size

