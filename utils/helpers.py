# 입력 검증, ISBN 검증, 출력 포맷팅 같은 공통 함수

from models.base_book import Book

def get_string(user_input):
    if user_input == "":
        print("아무것도 입력되지 않았습니다.")
        return False

    if not isinstance(user_input, str):
        print("문자열만 입력 가능합니다.")
        return False
    
    else: 
        return user_input


def get_valid_integer(value):
    if not value.isdigit():
        print("숫자만 입력 가능합니다.")
        return False
    else: 
        return int(value)


def isbn_check(isbn):
    if not isbn.digit():
        print("ISBN은 숫자만 입력할 수 있습니다.")
        return False
    
    elif len(isbn) != 13:
        print("ISBN 숫자 13자리를 입력하세요.")
        return False
    
    else:
        return isbn


def yes_or_not(user_input):
    if user_input == "":
        print("아무것도 입력되지 않았습니다.")
        return False

    if not isinstance(user_input, str):
        print("문자열만 입력 가능합니다.")
        return False

    if user_input != "y" and user_input != "n":
        print("y 혹은 n만 입력해주세요.")
        return False