def solution(myString, pat):
    answer = 0
    
    if pat.upper() in myString.upper() :
        return 1
    else :
        return 0
    
    return answer