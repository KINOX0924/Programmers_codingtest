def solution(binomial):
    answer = 0
    number_1 = ""
    number_2 = ""
    operator = ""
    
    for item in binomial :
        if item in "1234567890" and operator == "" :
            number_1 += item
        elif item in "1234567890" and operator != "" :
            number_2 += item
        elif item in r"+-*" :
            operator += item
    
    if operator == "+" :
        answer = int(number_1) + int(number_2)
    elif operator == "-" :
        answer = int(number_1) - int(number_2)
    elif operator == "*" :
        answer = int(number_1) * int(number_2)
            
    return answer