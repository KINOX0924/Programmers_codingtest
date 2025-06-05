def solution(my_string):
    answer   = []
    str_list = []
    
    while len(str_list) < 52 :
        str_list.append(0)
    
    for word in my_string :
        if ord(word) >= 65 and ord(word) <= 90 :
            str_list[ord(word) - 65] += 1
        elif ord(word) >= 97 and ord(word) <= 122 :
            str_list[ord(word) - 71] += 1
    
    answer = str_list
            
    
    return answer