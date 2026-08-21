import datetime # 대여 반납 처리시 처리 시간 기록용
from models.base_book import Book 
from models.specialized_books import Paperback, Hardcover, Ebook, Audiobook
from utils.helpers import get_string, get_valid_integer, isbn_check

def main():
        book_collection = {} # 도서 리스트 담을 딕셔너리 -- base_book.Book class와 연결
        rental_history = [] #set이 들어가는 리스트, (ISBN, 처리시간, 대여/반납)

        
        while True:
                print("=" * 30)
                print("도서 관리 시스템")
                print("=" * 30)
                print("원하는 메뉴를 선택해 주세요.")
                print("=" * 30)
                print("① 도서 등록")
                print("② 전체 도서 조회") 
                print("③ 도서 검색")
                print("④ 대여/반납 처리") # 대여·반납 시 발생 데이터(ISBN, 처리 시간 등)를 변경 불가능한 **튜플(Tuple)**로 묶어 **리스트(List)**에 순차 저장
                print("⑤ 통계 조회") # 월간 대여 통계, 최다 대여 도서 목록 콘솔 출력
                print("⑥ 종료")
                print("=" * 30)

                menu = get_valid_integer(input("원하는 메뉴 번호를 입력하세요: "))

#-----------------menu 1 도서 등록

                if menu == 1: # 도서 등록 -> 책 제목, 작가명, isbn 입력 -> isbn_check()로 isbn 검증 -> PaperBook 또는 Ebook 객체 생성 -> book_catalog[ISBN] = 객체

                        print("① 도서 등록을 시작합니다. ")

#-----------------isbn 입력                
                        while True:
                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: ")) # ISBN → check dictionary → title → author → create Book → store

                                if isbn is False:
                                        continue

                                if isbn in book_collection.keys():
                                        print("이미 존재하는 ISBN입니다.")
                                        continue

                                
                                print(f"ISBN[{isbn}]이 입력되었습니다.")
                                break
#-----------------book title
                        title = get_string(input("책 제목을 입력하세요:"))
                        print(f"책 제목[{title}](이)가 입력되었습니다.") #only the strings
#-----------------book author
                        author = get_string(input("작가명을 입력하세요:")) #only the strings
                        print(f"작가명 [{author}](이)가 입력되었습니다.")

#-----------------book type
                        print("① 페이퍼백 | ② 하드커버 | ③ 이북 | ④ 오디오북 ")

                        while True:
                                book_type = get_valid_integer(input("등록하는 책의 종류를 입력하세요: ")) 

                                if book_type is False:
                                        continue

                                if book_type not in range(1, 5):
                                        print("1~4까지의 숫자만 입력 가능합니다.")
                                        continue

                                if book_type == 1:

                                        while True:
                                                paperback_page = get_valid_integer(input("총 페이지를 입력하세요: "))
                                                if paperback_page is False:
                                                        continue
                                                book = Paperback(title, author, isbn, paperback_page)
                                                break

                                elif book_type == 2:
                                        while True:
                                                hardcover_page = get_valid_integer(input("총 페이지를 입력하세요: "))
                                                if hardcover_page is False:
                                                        continue
                                                book = Hardcover(title, author, isbn, hardcover_page)
                                                break

                                elif book_type == 3:
                                        while True:
                                                ebook_size = get_valid_integer(input("총 파일 크기를 입력하세요: "))
                                                if ebook_size is False:
                                                        continue
                                                book = Ebook(title, author,isbn, ebook_size)
                                                break

                                elif book_type == 4:
                                        while True:
                                                audiobook_size = get_valid_integer(input("총 파일 크기를 입력하세요: "))
                                                if audiobook_size is False:
                                                        continue
                                                book = Audiobook(title, author, isbn, audiobook_size)
                                                break

                                break

                        book_collection[isbn] = book
                        
                        print("도서 등록이 완료되었습니다.")
                        print(book)


#-----------------menu 2                        
                elif menu == 2:
                        print("② 전체 도서 조회를 시작합니다.")
                        if not book_collection:
                                print("현재 등록된 도서가 없습니다.")
                        else:
                                print("=" * 30)
                                print("전체 도서 목록")
                                print("=" * 30)

                                for index, (isbn, book) in enumerate(book_collection.items(), start=1): # __str__ in base_book.py
                                        print(f"no.{index} | {book}")

#-----------------menu 3
                elif menu == 3: # 도서 검색 -> book isbn 비교 (dict.keys())
                        print("③ 도서 검색을 시작합니다.")

                        if not book_collection:
                                print("현재 등록된 도서가 없습니다.")
                        else:
                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: ")) 

                                if isbn in book_collection:
                                        book = book_collection[isbn]
                                        print("도서 검색 완료!") # 대여 여부 추가?
                                        print(book)

                                else: 
                                        print("해당 ISBN의 도서가 없습니다.")


#-----------------menu 4
                elif menu == 4: # 대여/반납 처리 -> 
                        print("④ 대여/반납 처리를 시작합니다.")

                        if not book_collection:
                                print("현재 등록된 도서가 없습니다.")
                        else:
                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: "))   

                                if isbn in book_collection:
                                        book = book_collection[isbn]
                                else:
                                        print("해당 ISBN의 도서가 없습니다.") 

                                while True:

                                        if book.is_rented is False:
                                                print("대여 가능한 책입니다.")
                                
                                                answer = yes_or_not(input("해당 책을 대여하시겠습니까? (y/n)"))
                                        if answer == "y":
                                                book.is_rented = True
                                                print(f"[{book}] 도서 대여가 완료되었습니다.") 
                                        if answer == "n":

                                        else:
                                                print("이미 대여된 책입니다.")
                                                break




#-----------------menu 5
                elif menu == 5: # 월간 대여 통계, 최대 대여 도서 목록 콘솔 출력
                        print("⑤ 통계 조회를 시작합니다.")

#-----------------menu 6
                elif menu == 6:
                        print("⑥ 도서 관리 시스템을 종료합니다.")
                        break


                        
                        
                

if __name__ == "__main__":
        main()
