def solution(num_list):
    answer = 0
    count  = 0
    temp   = 0
    
    for number in num_list :
        temp = number
        while temp != 1 :
            if temp % 2 == 0 :
                temp = temp // 2
            elif temp % 2 == 1 :
                temp = (temp - 1) // 2
            count += 1
    
    return count