def solution(n):
    pizza       = 1
    pizza_slice = 6
    
    if   n == 0 :
        pizza = 0
    elif n == 1 or n == 2 or n == 3 or n == 6 :
        pizza = 1
    else :
        while True :
            pizza_slice += 6
            pizza += 1
            if pizza_slice % n == 0 :
                break
    
    return pizza