def solution(n):
    pizza = 0
    pizza_slice = 7
    
    if   n == 0 :
        pizza = 0
    elif n >= 1 and n <= 7 :
        pizza = 1
    else :
        while True :
            n -= pizza_slice
            pizza += 1
            if n <= 0 :
                break
        
    return pizza