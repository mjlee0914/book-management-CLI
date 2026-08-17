# 상위 Book 클래스

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def show_title(self): 
        print(self.title)

book_1 = Book("title", "author", "1234")
print(book_1.show_title())





