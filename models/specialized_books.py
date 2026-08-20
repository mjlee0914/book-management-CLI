from .base_book import Book



class Paperback(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.__pages = pages

    def rent(self):
        return self.__is_rented == True       



class Hardcover(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.__pages = pages

    def rent(self):
        return self.__is_rented == True

    

class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.__file_size = file_size

    def rent(self):
        return self.__is_rented == True
    
class Audiobook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.__file_size = file_size

    def rent(self):
        return self.__is_rented == True

