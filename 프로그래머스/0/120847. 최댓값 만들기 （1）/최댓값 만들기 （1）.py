from itertools import permutations

def calculator(num_list) :
    max = 0
    
    for numbers in num_list :
        if numbers[0] * numbers[1] >= max :
            max = numbers[0] * numbers[1]
    
    return max

def solution(numbers):
    num_list = list(permutations(numbers,2))
    
    max = calculator(num_list)
    
    return max