def solution(arr, queries):
    answer = []
    
    for query in queries :
        for i in range(query[0] , query[1] + 1) :
            arr[i] += 1
    return arr
    
    return answer
