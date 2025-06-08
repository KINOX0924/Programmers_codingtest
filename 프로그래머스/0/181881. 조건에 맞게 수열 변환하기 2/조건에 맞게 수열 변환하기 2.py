def solution(arr):
    answer = 0
    temp_list = list(arr)
    arr_list  = [None , list(arr)]
    
    while True :
        for index , number in enumerate(temp_list) :
            if number >= 50 and number % 2 == 0 :
                temp_list[index] = number // 2
            elif number < 50 and number % 2 == 1 :
                temp_list[index] = (number * 2) + 1
        arr_list.append(list(temp_list))
        
        if arr_list[-1] == arr_list[-2] :
            break
    
    for index , item in enumerate(arr_list) :
        if item == arr_list[-1] :
            return index - 1
    
    return answer