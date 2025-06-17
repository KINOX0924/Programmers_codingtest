def solution(n):
    number = 2
    total  = 1
    
    while total <= n :
        total *= number
        number += 1
        
    print(number)
    print(total)
    
    if number > 10 :
        number = 10
    else :
        number -= 2
    
    return number