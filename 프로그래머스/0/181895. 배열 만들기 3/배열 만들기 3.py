def solution(arr, intervals):
    answer = []
    
    for index in range(intervals[0][0] , intervals[0][1] + 1) :
        answer.append(arr[index])
    for index in range(intervals[1][0] , intervals[1][1] + 1) :
        answer.append(arr[index])
    
    return answer