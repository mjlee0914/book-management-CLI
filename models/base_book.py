# 상위 Book 클래스

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_rented = False


    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def rent(self):
        return self.__is_rented == True










