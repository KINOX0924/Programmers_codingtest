def solution(myString):
    answer = ''
    temp_list = []
    
    for word in myString :
        if word == "a" or word == "A" :
            temp_list.append(word.upper())
        else :
            temp_list.append(word.lower())
    
    answer = "".join(temp_list)
    
    return answer