def upperNlower(string) :
    string_list = [char for char in string]
    
    for index , char in enumerate(string_list) :
        if ord(char) >= 97 :
            string_list[index] = chr(ord(char)-32)
        else :
            string_list[index] = chr(ord(char)+32)
    
    return "".join(string_list)

def solution(my_string) :
    answer = upperNlower(my_string)
    
    return answer