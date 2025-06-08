def solution(strArr):
    length_dict = {}
    
    for item in strArr :
        if len(item) not in length_dict :
            length_dict[len(item)] = 1
        elif len(item) in length_dict :
            length_dict[len(item)] += 1
    
    value_list = list(length_dict.values())
    
    return max(value_list)