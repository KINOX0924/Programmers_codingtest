def solution(arr, k):
    answer = []
    temp   = []
    count  = 0
    
    while len(answer) != k :
        if count == len(arr) :
            break
        if arr[count] not in answer :
            answer.append(arr[count])
        count += 1
        
    while len(answer) < k :
        answer.append(-1)
        
    
    return answer