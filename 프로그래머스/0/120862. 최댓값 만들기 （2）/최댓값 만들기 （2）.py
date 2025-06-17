from itertools import permutations

def calculator(num_list) :
    max = -100000000
    
    for numbers in num_list :
        if int(numbers[0]) * int(numbers[1]) >= max :
            max = int(numbers[0]) * int(numbers[1])
    
    # print(max)  # 디버깅
    return max

def solution(numbers):
    dual_num_list = list(permutations(numbers, 2))
    # print(dual_num_list)    # 디버깅
    
    max_number = calculator(dual_num_list)
    
    return max_number