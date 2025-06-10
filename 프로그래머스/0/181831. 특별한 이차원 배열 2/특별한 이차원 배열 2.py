def solution(arr):
    result_list = []
    
    for i in range(0 , len(arr)) :
        for j in range(0 , len(arr[i])) :
            if arr[i][j] == arr[j][i] :
                result_list.append(1)
            else :
                result_list.append(0)
    
    if 0 in result_list :
        return 0
    else :
        return 1