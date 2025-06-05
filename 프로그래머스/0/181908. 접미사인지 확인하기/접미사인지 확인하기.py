def solution(my_string, is_suffix):
    answer = 0
    start  = 0
    str_list = []
    
    for i in range(0 , len(my_string)) :
        temp = ""
        for j in range(start , len(my_string)) :
            temp += my_string[j]
        start += 1
        str_list.append(temp)
    
    if is_suffix in str_list :
        answer = 1
    
    return answer