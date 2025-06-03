def solution(n):
    answer = 0
    
    if n % 2 == 0 :
        count = 2
        while count <= n :
            answer += count**2
            count  += 2
    else :
        count = 1
        while count <= n :
            answer += count
            count += 2
            
    return answer