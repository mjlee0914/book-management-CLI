def get_string(user_input):
    if user_input == "":
        print("아무것도 입력되지 않았습니다.")
        return False

    if not isinstance(user_input, str):
        print("문자열만 입력 가능합니다.")
        return False
    
    else: 
        return user_input


def get_valid_integer(user_input):
    if user_input == "":
        print("아무것도 입력되지 않았습니다.")
        return False
    
    if not user_input.isdigit():
        print("숫자만 입력 가능합니다.")
        return False
    
    else: 
        return int(user_input)


def isbn_check(user_input):
    if not user_input.isdigit():
        print("ISBN은 숫자만 입력할 수 있습니다.")
        return False
    
    elif len(user_input) != 13:
        print("ISBN 숫자 13자리를 입력하세요.")
        return False
    
    else:
        return user_input


def yes_or_no(user_input):

    if user_input == "":
        print("아무것도 입력되지 않았습니다.")
        return None

    lower_case = user_input.lower() 

    if lower_case != "y" and lower_case != "n":
        print("y 혹은 n만 입력해주세요.")
        return None 
        
    if lower_case == "y":
        return True

    if lower_case == "n":
        return False 
    


