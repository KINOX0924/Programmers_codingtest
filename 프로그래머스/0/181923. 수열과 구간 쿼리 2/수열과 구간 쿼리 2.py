def solution(arr, queries):
    answer   = []
    
    for i in range(0,len(queries)) :
        min_list = []
        for j in range(queries[i][0] , queries[i][1] + 1) :
            if arr[j] > queries[i][2] :
                min_list.append(arr[j])
        if len(min_list) == 0 :
            answer.append(-1)
        elif len(min_list) >= 1 :
            answer.append(min(min_list))

    return answer