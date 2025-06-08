def solution(arr, delete_list):
    num_list = []
    
    for number in arr :
        if number not in delete_list :
            num_list.append(number)
    
    return num_list