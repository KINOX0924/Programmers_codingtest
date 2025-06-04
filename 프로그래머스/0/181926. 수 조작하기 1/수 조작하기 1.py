def solution(n, control):
    answer = 0
    
    for key in control :
        if key == "w" :
            n += 1
        elif key == "s" :
            n -= 1
        elif key == "d" :
            n += 10
        else :
            n -= 10    
    answer = n
    
    return answer