def solution(numbers, k):
    count     = 1
    now_throw = 1
    
    while count < k :
        now_throw += 2
        if now_throw > len(numbers) :
            now_throw -= len(numbers)
        count     += 1
    
    return now_throw