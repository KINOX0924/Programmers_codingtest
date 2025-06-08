def solution(arr):
    answer = []
    index  = 0
    
    while index < len(arr) :
        if len(answer) == 0 :
            answer.append(arr[index])
        elif len(answer) >= 1 and answer[-1] == arr[index] :
            answer.pop()
        elif len(answer) >= 1 and answer[-1] != arr[index] :
            answer.append(arr[index])
        index += 1
    
    if len(answer) == 0 :
        answer.append(-1)
    
    return answer