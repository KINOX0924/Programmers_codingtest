def solution(my_string):
    num_list = []
    
    for char in my_string :
        if char.isdigit() :
            num_list.append(int(char))
    
    return list(sorted(num_list))