def solution(n, k):
    service_drink = 0
    sum_payment   = 0
    
    while n >= 1 :
        if n >= 10 :
            sum_payment += 120000
            n -= 10
            service_drink += 1
        elif n != 0 :
            sum_payment += 12000
            n -= 1
    
    k -= service_drink
    sum_payment += (k*2000)
    
    return sum_payment