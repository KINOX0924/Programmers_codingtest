def solution(arr, idx):
    answer = 0
    
    for index in range(0 , len(arr)) :
        if index >= idx and arr[index] == 1 :
            answer = index
            return answer
        else :
            answer = -1
    
    return answer