def solution(my_string, overwrite_string, s):
    answer = ''
    
    change_list = []
    change_list_2 = []
    
    for word in my_string :
        change_list.append(word)
        
    for word in overwrite_string :
        change_list_2.append(word)
    
    index = 0
    
    while index != len(change_list_2) :
        change_list[s] = change_list_2[index]
        s += 1
        index += 1
    
    answer = "".join(change_list)
    
    return answer