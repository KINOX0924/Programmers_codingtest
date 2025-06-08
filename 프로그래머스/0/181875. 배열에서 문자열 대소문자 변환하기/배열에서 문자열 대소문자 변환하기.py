def solution(strArr):
    answer = []
    
    for index , string in enumerate(strArr) :
        if index % 2 == 0 :
            strArr[index] = string.lower()
        else :
            strArr[index] = string.upper()
    
    answer = strArr
    
    return answer