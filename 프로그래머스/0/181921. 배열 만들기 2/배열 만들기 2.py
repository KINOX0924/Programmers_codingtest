def solution(l, r):
    answer = []
    first_numbers = []
    
    for number in range(l , r + 1) :
        if number % 5 == 0 or number % 10 == 0 :
            first_numbers.append(number)
    
    for number in first_numbers :
        if "1" not in str(number) and "2" not in str(number) and "3" not in str(number) and  "4" not in str(number) and  "6" not in str(number) and  "7" not in str(number) and  "8" not in str(number) and  "9" not in str(number) :
            answer.append(number)
    
    if len(answer) == 0 :
        answer.append(-1)
    
    return answer