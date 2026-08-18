# 입력 검증, ISBN 검증, 출력 포맷팅 같은 공통 함수

from models.base_book import Book

def get_string(user_input):
    if user_input == "":
        print("아무것도 입력되지 않았습니다.")
        return False
    else: 
        return user_input


def get_valid_integer(value):
    if not value.isdigit():
        print("숫자를 입력해 주세요.")
        return False
    else: 
        return int(value)


def isbn_check(isbn):

    if not isbn.isdigit():
        print("ISBN은 숫자만 입력할 수 있습니다."
        return False
        
    elif len(isbn) != 13:
        print("ISBN 숫자 13자리를 입력하세요.")
        return False
        
    else:
        return isbn

    
