def solution(num_list):
    answer = 0
    sum = 0
    mul = 0
    
    for number in num_list :
        sum += number
        if mul == 0 :
            mul += number
        elif mul != 0 :
            mul = mul * number
    sum = sum**2
    
    if sum < mul :
        answer = 0
    elif sum > mul :
        answer = 1
    
    
    return answer