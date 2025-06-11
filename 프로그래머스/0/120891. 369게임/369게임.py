def solution(order):
    clap_timing = ["3","6","9"]
    result = 0
    
    for word in str(order) :
        if word in clap_timing :
            result += 1
    
    return result