def solution(myStr):
    answer = []
    temp   = ""
    
    for word in myStr :
        if word in "abc" and temp != "" :
            answer.append(temp)
            temp = ""
        elif word not in "abc" :
            temp += word
    
    if temp != "" :
        answer.append(temp)
    elif temp == "" :
        answer.append("EMPTY")
    
    return answer