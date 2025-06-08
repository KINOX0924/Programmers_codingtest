def solution(myString, pat):
    answer = 0
    string = ""
    
    for word in myString :
        if word == "A" :
            string += "B"
        elif word == "B" :
            string += "A"
    
    if pat in string :
        answer = 1
    
    return answer