def solution(a, d, included):
    answer = 0
    
    for bool in included :
        if bool == True :
            answer += a
        a += d
    
    return answer