# 입력 검증, ISBN 검증, 출력 포맷팅 같은 공통 함수

from models.base_book import Book

def get_string(prompt):
    if prompt == "":
        print("아무것도 입력되지 않았습니다.")
        return False
    else: 
        return prompt




def get_valid_integer(prompt):
    if not prompt.isdigit():
        print("숫자를 입력해 주세요.")
        return False
    elif
    


def isbn_check(isbn):
    if len(isbn) != 13:
        print("유효한 ISBN 숫자가 아닙니다")
        return False
    else:
        return isbn

    