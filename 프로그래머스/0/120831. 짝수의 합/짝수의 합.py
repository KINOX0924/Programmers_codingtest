def solution(n):
    sum_number = 0
    
    for num in range(0 , n + 1) :
        if num % 2 == 0 :
            sum_number += num
    
    # print(sum_number)   # Debug
    
    return sum_number