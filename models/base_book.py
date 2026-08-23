# 상위 Book 클래스

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_rented = False

    def __str__(self):
        return f"ISBN: {self.__isbn} | 제목: {self.__title} | 작가: {self.__author}"

    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_rented(self):        # 대여 여부 확인
        return self.__is_rented

    def rent(self):
        return self.__is_rented == True

    def return_book(self):
        return self.__is_rented == False

    







