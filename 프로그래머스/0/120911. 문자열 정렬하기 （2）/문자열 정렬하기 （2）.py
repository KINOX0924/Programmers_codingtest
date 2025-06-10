def solution(my_string):
    my_string = [ char for char in my_string.lower() ]
    string = "".join(sorted(my_string))
    
    return string