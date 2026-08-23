from .base_book import Book



class Paperback(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.__pages = pages
        
    def __str__(self):
        return f"{super().__str__()} | 총 페이지: {self.__pages}쪽"
     



class Hardcover(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.__pages = pages

    def __str__(self):
        return f"{super().__str__()} | 총 페이지: {self.__pages}쪽"

    

class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.__file_size = file_size

    def __str__(self):
        return f"{super().__str__()} | 파일 크기: {self.__file_size}MB"

    
class Audiobook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.__file_size = file_size

    def __str__(self):
        return f"{super().__str__()} | 파일 크기: {self.__file_size}MB"
