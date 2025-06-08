def solution(my_string, alp):
    answer = ''
    temp_list = []
    
    for word in my_string :
        if word == alp.upper() or word == alp.lower() :
            temp_list.append(word.upper())
        else :
            temp_list.append(word.lower())
    
    answer = "".join(temp_list)
    
    return answer