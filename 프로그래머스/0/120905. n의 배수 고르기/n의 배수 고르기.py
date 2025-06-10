def solution(n, numlist):
    result = []
    
    for number in numlist :
        if number % n == 0 :
            result.append(number)
    
    return result