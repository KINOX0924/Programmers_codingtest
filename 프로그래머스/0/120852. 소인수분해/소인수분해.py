def calculator(number) :
    prime_factors = []
    now_factor    = 2
    
    while number != 1 :
        if number % now_factor == 0 :
            number = number // now_factor
            if now_factor not in prime_factors :
                prime_factors.append(now_factor)
        else :
            now_factor += 1
            
    # print(prime_factors)    # 디버깅
    
    return prime_factors

def solution(n):
    prime_factors = calculator(n)
    
    return prime_factors