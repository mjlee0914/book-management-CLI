# main.py 실행 시 while문 + input()으로 메뉴(①도서 등록 ②전체 도서 조회 ③도서 검색 ④대여/반납 처리 ⑤종료) 표시, 입력값에 따라 로직 분기


while True:
    try:


        menu = int(input(f"안녕하세요, 도서 관리 시스템입니다. 무엇을 도와드릴까요?\n① 도서 등록 ② 전체 도서 조회 ③ 도서 검색 ④ 대여/반납 처리 ⑤ 통계 조회 ⑥ 종료\n원하시는 메뉴 번호를 입력해주세요:" ))

        if menu == 1:
            print("도서를 등록합니다.")
        elif menu == 2:
            print("전체 도서를 조회합니다.")
        elif menu == 3:
            print("도서를 검색합니다.")
        elif menu == 4:
            print("대여 또는 반납하기를 원하는 책 정보를 입력해 주세요.")
        elif menu == 5:
            print(f"월간 대여 통계: \n최대 대여 콘솔 목록")
            break
        elif menu == 6:
            print("도서 관리 시스템을 종료합니다.")
            break
        else:
            print("1 ~ 6 사이의 번호만 입력 가능합니다.")


    except ValueError:
        print(f"숫자만 입력 가능합니다.\n예) 1")