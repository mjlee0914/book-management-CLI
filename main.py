import datetime # 대여 반납 처리시 처리 시간 기록용
from models.base_book import Book 
from models.specialized_books import Paperback, Hardcover, Ebook, Audiobook
from utils.helpers import get_string, get_valid_integer, isbn_check

def main():
        book_collection = {} # 도서 리스트 담을 딕셔너리 -- base_book.Book class와 연결
        rental_history = [] #튜플이 들어가는 리스트, (ISBN, 처리시간, 대여/반납)

        
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

                menu = get_valid_integer(input("원하는 메뉴 번호를 입력하세요: "))
                if menu == 1: # 도서 등록 -> 책 제목, 작가명, isbn 입력 -> isbn_check()로 isbn 검증 -> PaperBook 또는 Ebook 객체 생성 -> book_catalog[ISBN] = 객체

                        print("① 도서 등록을 시작합니다. ")

                        isbn = isbn_check(input("ISBN을 입력하세요: ")) # ISBN → check dictionary → title → author → create Book → store
                        while True:
                                if isbn in book_collection.keys():
                                        print("이미 존재하는 ISBN입니다.")
                                        continue

                                else: 
                                        book_collection[isbn] = "" # title, author, book type, pages, file size
                                        break

                        title = get_string(input("책 제목을 입력하세요:")) #only the strings

                        author = get_string(input("작가명을 입력하세요:")) #only the strings

                        print("=" * 20)
                        print("① 페이퍼백")
                        print("② 하드커버") 
                        print("③ 이북")
                        print("④ 오디오북")
                        print("=" * 20)

                        book_type = get_valid_integer(input("북 타입을 입력하세요: ")) 

                        while True:

                                if book_type == 1:
                                        paperback_page = input("총 페이지를 입력하세요: ")
                                        book = Paperback(title, author, isbn, paperback_page)
                                elif book_type == 2:
                                        hardcover_page = input("총 페이지를 입력하세요: ")
                                        book = Hardcover(title, author, isbn, hardcover_page)
                                elif book_type == 3:
                                        ebook_size = input("총 파일 크기를 입력하세요: ")
                                        book = Ebook(title, author,isbn, ebook_size)
                                elif book_type == 4:
                                        audiobook_size = input("총 파일 크기를 입력하세요: ")
                                        book = Audiobook(title, author, isbn, audiobook_size)

                                break

                        book_collection[isbn] = book
                        print("도서 등록이 완료되었습니다.")
                        print(f"ISBN: {isbn} |")






        
                        

                        
                elif menu == 2:
                         # 전체 도서 조회 -> isbn: 책 제목, 작가명, 북타입, 페이지수/파일크기 book_catalog 객체 하나씩 조회 for 문

                        pass

                elif menu == 3: # 도서 검색 -> book isbn 비교 (dict.keys())
                        pass

                elif menu == 4: # 대여/반납 처리 -> 
                        pass

                elif menu == 5: # 월간 대여 통계, 최대 대여 도서 목록 콘솔 출력
                        pass

                elif menu == 6:
                        print("도서 관리 시스템을 종료합니다.")
                        break


                        
                        
                

if __name__ == "__main__":
        main()
