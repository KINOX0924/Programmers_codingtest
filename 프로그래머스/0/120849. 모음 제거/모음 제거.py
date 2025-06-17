def solution(my_string):
    del_string = ""
    
    for char in my_string :
        if char not in "aeiou" :
            del_string += char
            
    return del_string