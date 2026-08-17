# main.py 실행 시 while문 + input()으로 메뉴(①도서 등록 ②전체 도서 조회 ③도서 검색 ④대여/반납 처리 ⑤종료) 표시, 입력값에 따라 로직 분기
# CLI 실행 + 메뉴 선택 + 전체 프로그램 흐름
from models.base_book import Book

book_list = []

while True:
    try:


        menu = int(input(f"안녕하세요, 도서 관리 시스템입니다. 무엇을 도와드릴까요?\n① 도서 등록 ② 전체 도서 조회 ③ 도서 검색 ④ 대여/반납 처리 ⑤ 통계 조회 ⑥ 종료\n원하시는 메뉴 번호를 입력해주세요:" ))

        if menu == 1:
            print("도서를 등록합니다.")

            book_title = input("책 제목을 입력해주세요. : ")
            print(f"책 제목: {book_title}")

            book_author = input("작가명을 입력해주세요. : ")
            print(f"책 제목: {book_title} | 작가명: {book_author}")

            while True:
                book_isbn = input("ISBN을 입력해주세요. : ") 

                if not book_isbn.isdigit():
                    print("숫자 13자리를 입력해주세요.")

                elif len(book_isbn) != 13:
                    print("숫자 13자리를 입력하세요.")

                else:
                    break
                    
            #if 문으로 중복된 도서가 없는지 확인, 확인 후 패스

                while True:
                    if 
            print(f"도서 등록 완료!\n책 제목: {book_title} | 작가명: {book_author} | ISBN: {book_isbn}")  
            book_list.append(Book(book_title, book_author, book_isbn))


        elif menu == 2:
            print("전체 도서를 조회합니다.")

            # 전체 도서 리스트 책 제목 | 작가명 | isbn으로 조회, 최신순/알파벳순 옵션
        


        elif menu == 3:
            print("도서를 검색합니다.")
            # 책 제목, 작가명, isbn으로 검색



        elif menu == 4:
            print("책 대여 혹은 반납 서비스")
            # 책 대여 / 반납 선택 -> 책 제목/작가명/isbn으로 조회 -> 대여 불가 or 반납 불가 여부 검색 -> 대여 가능 / 반납 가능 -> 대여/반납하시겠습니까? -> ~까지 대여 or 반납 완료 메시지

        elif menu == 5:
            print(f"월간 대여 통계: \n최대 대여 콘솔 목록")
            # 월간 대여 통계 (현시점 기준) or 최대 대여 책 목록 확인 옵션


        elif menu == 6:
            print("도서 관리 시스템을 종료합니다.")
            break


        else:
            print("1 ~ 6 사이의 번호만 입력 가능합니다.")

    except ValueError:
        print(f"숫자만 입력 가능합니다.\n예) 1")