import datetime # 대여 반납 처리시 처리 시간 기록용
from models.base_book import Book
from models.specialized_books import Paperback, Hardcover, Ebook, Audiobook
from utils.helpers import get_string, get_valid_integer, isbn_check, yes_or_not

def main():
        book_collection = {} 
        rental_history = [] 

        
        while True:
                print("=" * 30)
                print("도서 관리 시스템")
                print("=" * 30)
                print("원하는 메뉴를 선택해 주세요.")
                print("=" * 30)
                print("① 도서 등록")
                print("② 전체 도서 조회") 
                print("③ 도서 검색")
                print("④ 대여/반납 처리") 
                print("⑤ 통계 조회")
                print("⑥ 종료")
                print("=" * 30)

                menu = get_valid_integer(input("원하는 메뉴 번호를 입력하세요: "))

#-----------------------------------------------------------------menu 1 도서 등록

                if menu == 1: 

                        print("① 도서 등록을 시작합니다. ")

#-----------------isbn 입력                
                        while True:
                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: ")) 

                                if isbn is False:
                                        continue

                                if isbn in book_collection.keys():
                                        print("이미 존재하는 ISBN입니다.")
                                        continue

                                
                                print(f"ISBN[{isbn}]이 입력되었습니다.")
                                break
#-----------------book title
                        title = get_string(input("책 제목을 입력하세요:"))
                        print(f"책 제목[{title}](이)가 입력되었습니다.") 
#-----------------book author
                        author = get_string(input("작가명을 입력하세요:")) 
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


#-----------------------------------------------------------------menu 2 전체 도서 조회                 
                elif menu == 2:
                        print("② 전체 도서 조회를 시작합니다.")
                        if not book_collection:
                                print("현재 등록된 도서가 없습니다.")
                        else:
                                print("=" * 30)
                                print("전체 도서 목록")
                                print("=" * 30)

                                for index, (isbn, book) in enumerate(book_collection.items(), start=1): # __str__ in base_book.py
                                        print(f"No.{index} | {book}")

#-----------------------------------------------------------------menu 3 도서 검색 
                elif menu == 3: 
                        print("③ 도서 검색을 시작합니다.")

                        if not book_collection:
                                print("현재 등록된 도서가 없습니다.")
                        else:
                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: ")) 

                                if isbn in book_collection:
                                        book = book_collection[isbn]
                                        print("도서 검색 완료!") # 대여 여부 추가?
                                        print(book)
                                        if book.is_rented():
                                                print("도서 대여 여부: 도서 대여 중")
                                        else:
                                                print("도서 대여 여부: 대여 가능")


#-----------------------------------------------------------------menu 4 대여/반납 처리
                elif menu == 4:
                        print("④ 대여/반납 처리를 시작합니다.")

                        if not book_collection: ## 예외처리?
                                print("현재 등록된 도서가 없습니다.")

                        else:
                                rent_or_return = get_valid_integer(input("대여를 원하시면 1, 반납을 원하시면 2를 입력해 주세요:"))

                                if rent_or_return == 1:
                                        print("[대여 프로세스]")
                                        while True:
                                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: "))   

                                                if isbn not in book_collection:
                                                        print("해당 ISBN의 도서가 없습니다.")
                                                        continue
                                                else:
                                                        book = book_collection[isbn]
                                                        break
                                                
                                        if not book.is_rented():
                                                print("대여 가능한 책입니다.")
                                                while True:                                                
                                                        answer = yes_or_not(input("해당 책을 대여하시겠습니까? (y/n)"))
                                                        if answer == "y":
                                                                book.rent()
                                                                rent_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                                rental_history.append((isbn, rent_time, "대여"))
                                                                print(f"[{book}] 도서 대여가 완료되었습니다.") 
                                                                break
                                                        else:
                                                                break
                                        else:
                                                print("이미 대여된 책입니다.")

                                elif rent_or_return == 2:
                                        print("[반납 프로세스]")
                                        while True:
                                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: "))   

                                                if isbn not in book_collection:
                                                        print("해당 ISBN의 도서가 없습니다.")
                                                        continue

                                                else:
                                                        book = book_collection[isbn]
                                                        break
                                                               
                                        if book.is_rented():
                                                print("반납 가능한 책입니다.")
                                                while True:  
                                                        answer = yes_or_not(input("해당 책을 반납하시겠습니까? (y/n)"))

                                                        if answer == "y":
                                                                book.return_book()
                                                                return_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                                rental_history.append((isbn, return_time, "반납"))
                                                                print(f"[{book}] 도서 반납이 완료되었습니다.")
                                                                break
                                                        else:
                                                                break
                                        else:
                                                print("아직 대여되지 않은 책입니다.")


#-----------------------------------------------------------------menu 5 통계 조회
                elif menu == 5: # 월간 대여 통계, 최대 대여 도서 목록 콘솔 출력
                        print("⑤ 통계 조회를 시작합니다.")



#-----------------------------------------------------------------menu 6 시스템 종료
                elif menu == 6:
                        print("⑥ 도서 관리 시스템을 종료합니다.")
                        break


                        
                        
                

if __name__ == "__main__":
        main()
