def solution(my_string, is_prefix):
    answer = 0
    end = 1
    temp = ""
    str_list = []
    
    for i in range(0 , len(my_string)) :
        temp = ""
        for j in range(0 , end) :
            temp += my_string[j]
        str_list.append(temp)
        end += 1
    
    if is_prefix in str_list :
        answer = 1
    
    return answer