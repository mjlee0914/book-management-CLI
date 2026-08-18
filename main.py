

import datetime # 대여 반납 처리시 처리 시간 기록용
from models.base_book import Book 
from models.specialized_books import PaperBook, Ebook
from utils.helpers import get_string, get_valid_integer, isbn_check

def main():
        book_catalog = {} # 도서 리스트 담을 딕셔너리 -- base_book.Book class와 연결
        rental_history = [] #튜플이 들어가는 리스트, (ISBN, 처리시간, 대여/반납)

        
        while True:
                print("=" * 20)
                print("도서 관리 시스템")
                print("=" * 20)
                print("원하는 메뉴를 선택해 주세요.")
                print("=" * 20)
                print("① 도서 등록")
                print("② 전체 도서 조회") 
                print("③ 도서 검색")
                print("④ 대여/반납 처리") # 대여·반납 시 발생 데이터(ISBN, 처리 시간 등)를 변경 불가능한 **튜플(Tuple)**로 묶어 **리스트(List)**에 순차 저장
                print("⑤ 통계 조회") # 월간 대여 통계, 최다 대여 도서 목록 콘솔 출력
                print("⑥ 종료")  

                menu = get_valid_integer(input(원하는 메뉴 번호를 입력하세요: ))
                if menu == 1: # 도서 등록 -> 책 제목, 작가명, isbn 입력 -> isbn_check()로 isbn 검증 -> PaperBook 또는 Ebook 객체 생성 -> book_catalog[ISBN] = 객체
                        
                elif menu == 2: # 전체 도서 조회 -> isbn, 책 제목, 작가명 쫘르륵 book_catalog 객체 하나씩 조회
                        pass
                elif menu == 3: # 도서 검색 -> book isbn 비교 
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
