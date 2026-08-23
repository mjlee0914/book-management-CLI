import datetime # 대여 반납 처리시 처리 시간 기록용
from models.specialized_books import Paperback, Hardcover, Ebook, Audiobook
from utils.helpers import get_string, get_valid_integer, isbn_check, yes_or_not

def main():
        book_collection = {} # ISBN을 key 값으로 받고, 나머지 정보를 value값으로 받는 dictionary로 정의 -> 도서 검색시 ISBN으로 조회 가능
        rental_history = []  # 대여 발생시마다 (isbn, return_time, "반납" 혹은 "대여")의 tuple을 정의하여 리스트에 append -> 각 책마다 대여 정보는 수정불가한 Tuple로, 대여 목록은 List로 정의하여 통계 조회가 가능함 
        rental_count = {} # ISBN을 key 값으로 받고, 해당 ISBN에 해당하는 도서의 대여 횟수를 value 값으로 추가함
        most_rented_books = [] 
        monthly_rental_stats = 0
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month        

        
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

                                        if book.is_rented():
                                                print("도서 대여 여부: 도서 대여 중")
                                        else:
                                                print("도서 대여 여부: 대여 가능")

#-----------------------------------------------------------------menu 3 도서 검색 
                elif menu == 3: 
                        print("③ 도서 검색을 시작합니다.")

                        if not book_collection:
                                print("현재 등록된 도서가 없습니다.")

                        else:
                                go_back_to_main_menu = False

                                while True:
                                        isbn = isbn_check(input("13자리 ISBN을 입력하세요: ")) 

                                        if isbn is False:
                                                continue

                                        if isbn not in book_collection:
                                                print("해당 ISBN의 도서가 없습니다.")
                                                print("메인 메뉴로 돌아가시겠습니까? (y/n)")
                                                answer = yes_or_not(input("y -> 메인 메뉴 돌아가기, n -> ISBN 다시 입력하기"))

                                                if answer:
                                                        go_back_to_main_menu = True
                                                        print("메인 메뉴로 돌아갑니다.")
                                                        break

                                                if answer is None:
                                                        continue

                                                else:
                                                        break

                                        if go_back_to_main_menu:
                                                break 
                                        
                                        book = book_collection[isbn]
                                        break

                                if not go_back_to_main_menu:                        
                                        print("도서 검색 완료!") 
                                        print(book)

                                        if book.is_rented():
                                                print("도서 대여 여부: 도서 대여 중")
                                        else:
                                                print("도서 대여 여부: 대여 가능")

                                


#-----------------------------------------------------------------menu 4 대여/반납 처리
                elif menu == 4:
                        print("④ 대여/반납 처리를 시작합니다.")

                        if not book_collection: 
                                print("현재 등록된 도서가 없습니다.")

                        else:
                                while True:
                                        rent_or_return = get_valid_integer(input("대여를 원하시면 1, 반납을 원하시면 2를 입력해 주세요:"))

                                        if rent_or_return != 1 and rent_or_return != 2:
                                                print("숫자 1 혹은 2만 입력 가능합니다.")
                                                continue

                                        break

                                if rent_or_return == 1:
                                        print("[대여 프로세스]")
                                        while True:
                                                isbn = isbn_check(input("13자리 ISBN을 입력하세요: "))   

                                                if isbn is False:
                                                        continue

                                                try:    
                                                        book = book_collection[isbn]

                                                except KeyError:
                                                        print("해당 ISBN의 도서가 없습니다.")
                                                        continue

                                                else:
                                                        break
                                                
                                        if not book.is_rented():
                                                print("대여 가능한 책입니다.")
                                                while True:                                                
                                                        answer = yes_or_not(input("해당 책을 대여하시겠습니까? (y/n)"))
                                                        
                                                        if answer:
                                                                book.rent()
                                                                rent_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                                rental_history.append((isbn, rent_time, "대여"))
                                                                print(f"[{book}] 도서 대여가 완료되었습니다.") 
                                                                break

                                                        if answer is None:
                                                                continue

                                                        else:
                                                                print("대여 프로세스를 종료합니다.")
                                                                break
                                        else:
                                                print("이미 대여된 책입니다.")

                                elif rent_or_return == 2:
                                        print("[반납 프로세스]")
                                        has_rented_book = False

                                        for book in book_collection.values():
                                                if book.is_rented():
                                                       has_rented_book = True
                                                       break

                                        if not has_rented_book:
                                                print("대여중인 책이 존재하지 않습니다. ")

                                        else:

                                                while True:
                                                        isbn = isbn_check(input("13자리 ISBN을 입력하세요: "))   

                                                        if isbn is False:
                                                                continue

                                                        try:    
                                                                book = book_collection[isbn]

                                                        except KeyError:
                                                                print("해당 ISBN의 도서가 없습니다.")
                                                                continue

                                                        else:
                                                                break

                                                                                
                                                if book.is_rented():
                                                        print("반납 가능한 책입니다.")
                                                        while True:  
                                                                answer = yes_or_not(input("해당 책을 반납하시겠습니까? (y/n)"))

                                                                if answer:
                                                                        book.return_book()
                                                                        return_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                                        rental_history.append((isbn, return_time, "반납"))
                                                                        print(f"[{book}] 도서 반납이 완료되었습니다.")
                                                                        break

                                                                if answer is None:
                                                                        continue

                                                                else:
                                                                        print("반납 프로세스를 종료합니다.") 
                                                                        break
                                                else:
                                                        print("아직 대여되지 않은 책입니다.")


#-----------------------------------------------------------------menu 5 통계 조회
                elif menu == 5: # 월간 대여 통계, 최대 대여 도서 목록 콘솔 출력

                        if not rental_count and rental_history == []:
                                print("대여 기록이 존재하지 않습니다.")
                                print("메인 메뉴로 돌아갑니다.")
                                continue
                        else:

                                print("⑤ 통계 조회를 시작합니다.")

                        while True:
                                menu5_answer = get_valid_integer(input("월간 대여 통계 조회를 원하시면 1, 최대 대여 도서 목록 조회를 원하시면 2를 입력해 주세요:"))

                                if menu5_answer != 1 and menu5_answer != 2:
                                        print("숫자 1 혹은 2만 입력 가능합니다.")
                                        continue

                                break

                        if menu5_answer == 1:
                                                        # 월간 대여 통계 보기
                                for isbn, time, rental_type in rental_history:
                                        if rental_type == "대여":


                                                date_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                                                month_num = date_time.month
                                                year_num = date_time.year                                       

                                                if current_year == year_num  and month_num == current_month :
                                                        monthly_rental_stats += 1
                                print("*" * 20)
                                print("[월간 대여 통계 조회]")
                                print(f"{current_year}년 {current_month}월 대여 통계")
                                print(f"총 대여 횟수: {monthly_rental_stats}")
                                print("*" * 20)      

                        # 최대 대여 도서 목록 보기
                        elif menu5_answer == 2:
                                for isbn, _, rental_type in rental_history: #tuple 돌면서 1, 2, 3값 가져오기
                                        
                                        if rental_type == "대여":
                                                if isbn not in rental_count:
                                                        rental_count[isbn] = 1
                                                else:
                                                        rental_count[isbn] += 1

                                if rental_count:

                                        max_rental_count = max(rental_count.values())
                                        for isbn, count in rental_count.items():
                                                if count == max_rental_count:
                                                        most_rented_books.append(book_collection[isbn])
                                        print("*" * 20)
                                        print("[최대 대여 도서 목록 조회]")
                                        print("최대 대여 도서:")
                                        for book in most_rented_books:
                                                print(book)
                                        print("*" * 20)
                                        print(f"최대 대여 횟수: 총 {max_rental_count}회")
                                        print("*" * 20)



        
#-----------------------------------------------------------------menu 6 시스템 종료
                elif menu == 6:
                        print("⑥ 도서 관리 시스템을 종료합니다.")
                        break


if __name__ == "__main__":
        main()
