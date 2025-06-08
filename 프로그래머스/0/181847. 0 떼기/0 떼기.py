def solution(n_str):
    number_list = []
    
    for number in n_str :
        if len(number_list) != 0 and number == "0" :
            number_list.append(number)
        elif number != "0" :
            number_list.append(number)
    
    answer = "".join(number_list)
    return answer