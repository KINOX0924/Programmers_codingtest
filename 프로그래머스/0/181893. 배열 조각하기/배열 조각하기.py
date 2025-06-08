def solution(arr, query):
    answer = []
    
    for index in range(0 , len(query)) :
        if index % 2 == 0 :
            temp = []
            for index_2 in range(0 , query[index] + 1) :
                temp.append(arr[index_2])
            arr = temp
        elif index % 2 == 1 :
            temp = []
            for index_2 in range(query[index] , len(arr)) :
                temp.append(arr[index_2])
            arr = temp
    
    answer = arr
    
    return answer