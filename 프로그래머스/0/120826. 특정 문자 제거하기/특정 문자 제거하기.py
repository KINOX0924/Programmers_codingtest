def solution(my_string, letter):
    cutted_string = ""
    
    for char in my_string :
        if char != letter :
            cutted_string += char
    
    return cutted_string