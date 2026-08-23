class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_rented = False

    def __str__(self):
        return f"ISBN: {self.__isbn} | 제목: {self.__title} | 작가: {self.__author}"

    def is_rented(self):        
        return self.__is_rented

    def rent(self):
        self.__is_rented = True
        return self.__is_rented 

    def return_book(self):
        self.__is_rented = False
        return self.__is_rented

    



