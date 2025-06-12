def countChar(string) :
    string_list = []
    
    for ch in string :
        if ch not in string_list :
            string_list.append(ch)
    
    print(string_list)
    
    return "".join(string_list)
    
def solution(my_string) :
    answer = countChar(my_string)
    
    return answer