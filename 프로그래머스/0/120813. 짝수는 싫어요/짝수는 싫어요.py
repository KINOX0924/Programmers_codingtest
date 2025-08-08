def solution(n):
    odd_list = []
    
    for num in range(1 , n + 1) :
        if num % 2 == 1 :
            odd_list.append(num)
    
    return odd_list