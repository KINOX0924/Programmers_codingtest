def solution(a, b, c):
    answer = 0
    
    if (a == b and a != c) or (a == c and a != b) or (c == b and a != c) :
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    elif (a == b) and (b == c) :
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    else :
        answer = a + b + c
    
    return answer