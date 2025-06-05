def solution(n, k):
    answer = []
    
    for i in range(0, n + 1) :
        if i != 0 and i % k == 0 :
            answer.append(i)
    
    
    return answer