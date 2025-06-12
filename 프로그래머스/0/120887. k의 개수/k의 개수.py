def solution(i, j, k):
    count = 0
    
    for number in range(i , j + 1) :
        for char in str(number) :
            if str(k) == char :
                count += 1
            
    return count