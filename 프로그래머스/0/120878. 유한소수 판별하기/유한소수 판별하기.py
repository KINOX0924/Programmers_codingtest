def getDivisor(number) :
    common_list = [ num for num in range(1 , number+1) if number % num == 0 ]
    # print(common_list)  # 디버깅
    
    return common_list

def getMaxdivisor(common_list1 , common_list2) :
    inter_list = list(set(common_list1).intersection(common_list2))
    # print(inter_list)   # 디버깅
    
    return max(inter_list)

def getPrimefactors(denominator) :
    prime_factors = []
    divider = 2
    
    while denominator > 1 :
        if denominator % divider == 0 :
            denominator = denominator // divider
            prime_factors.append(divider)
        else :
            divider += 1
    
    # print(prime_factors)    # 디버깅
    return list(set(prime_factors))
        
def solution(a, b):
    a_common_list = getDivisor(a)   # 분자
    b_common_list = getDivisor(b)   # 분모
    
    max_divisor = getMaxdivisor(a_common_list , b_common_list)
    # print(max_divisor)  # 디버깅
    
    prime_factors = getPrimefactors(b // max_divisor)
    print(prime_factors)    # 디버깅
    
    for prime_factor in prime_factors :
        print(prime_factor)
        if prime_factor != 2 and prime_factor != 5 :
            return 2
        
    return 1