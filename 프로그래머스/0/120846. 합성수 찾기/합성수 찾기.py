def getFactor(number) :
    temp_list   = []
    factor_list = []
    num         = 4
    
    while num <= number :
        for i in range(1 , num + 1) :
            if num % i == 0 :
                temp_list.append(i)
        if len(temp_list) >= 3 :
            factor_list.append(num)
        temp_list = []
        num += 1
        
    return len(factor_list)

def solution(n):
    if n <= 3 :
        return 0
    
    factor_count = getFactor(n)
    
    return factor_count