def solution(my_string):
    reverse_string = "".join([ x for x in my_string[-1::-1]])
    
    return reverse_string