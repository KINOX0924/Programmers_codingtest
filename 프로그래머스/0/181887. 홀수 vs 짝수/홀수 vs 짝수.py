def solution(num_list):
    answer = 0
    count  = 1
    
    even_total = 0
    odd_total  = 0
    
    for number in num_list :
        if count % 2 == 1 :
            even_total += number
        else :
            odd_total  += number
        count += 1
    
    if even_total > odd_total :
        return even_total
    elif even_total < odd_total :
        return odd_total
    else :
        return even_total
    
    return answer