def solution(my_string):
    answer = []
    temp   = ""
    
    for word in my_string :
        if word == " " :
            answer.append(temp)
            temp = ""
        elif word != " " :
            temp += word
    
    answer.append(temp)
    
    return answer