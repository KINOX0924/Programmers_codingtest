def solution(num_list):
    answer = 0
    
    even_str = ""
    odd_str  = ""
    
    for num in num_list :
        if num % 2 == 0 :
            even_str += str(num)
        else :
            odd_str += str(num)
    
    answer = int(even_str) + int(odd_str)
    
    return answer