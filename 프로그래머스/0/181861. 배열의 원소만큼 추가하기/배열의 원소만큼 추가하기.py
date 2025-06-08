def solution(arr):
    answer = []
    
    for number in arr :
        for i in range(0, number) :
            answer.append(number)
    
    return answer