def calculator(number) :
    normal_number = 1
    town_number   = 1
    
    while normal_number <= number :
        if "3" in str(town_number) or town_number % 3 == 0 :
            town_number += 1
        else :
            normal_number += 1
            town_number += 1
            
    return town_number -1

def solution(n):
    result_number = calculator(n)
    
    print(result_number)
    
    return result_number