# main.py 실행 시 while문 + input()으로 메뉴(①도서 등록 ②전체 도서 조회 ③도서 검색 ④대여/반납 처리 ⑤종료) 표시, 입력값에 따라 로직 분기
# CLI 실행 + 메뉴 선택 + 전체 프로그램 흐름
# isbn 기준 검색/처리
from models.base_book import Book
from models.specialized_books import PaperBook, Ebook
from utils.helpers import get_string, get_valid_integer, isbn_check


if __name__ == "__main__":
        main()
