def solution(num, total):
    num_list  = []
    sum_total = 0
    number = -100
    
    if num == 1 :
        num_list.append(total)
        return num_list
    
    while True :
        if len(num_list) < num :
            num_list.append(number)
            number += 1
        elif len(num_list) == num :
            if sum(num_list) == total :
                return num_list
            else :
                num_list.pop(0)