def solution(my_string, s, e):
    answer = ''
    str_list     = [ word for word in my_string ]
    
    reverse_list = []
    count = 0
    
    for i in range(e , s - 1 , -1) :
        reverse_list.append(str_list[i])
    
    for j in range(s , e + 1) :
        str_list[j] = reverse_list[count]
        count += 1
    
    answer = "".join(str_list)
    
    return answer