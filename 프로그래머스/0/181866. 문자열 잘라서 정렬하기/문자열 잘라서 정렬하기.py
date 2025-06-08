def solution(myString):
    answer = []
    temp   = ""
    
    for word in myString :
        if word == "x" :
            if temp != "" :
                answer.append(temp)
                temp = ""
        elif word != "x" :
            temp += word
            
    if temp != "" :
        answer.append(temp)
    
    answer = sorted(answer)
    
    return answer