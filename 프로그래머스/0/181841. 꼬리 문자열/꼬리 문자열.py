def solution(str_list, ex):
    answer_string = ""
    
    for string in str_list :
        if ex not in string :
            answer_string += string
    
    return answer_string