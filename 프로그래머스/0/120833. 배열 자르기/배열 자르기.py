def solution(numbers, num1, num2):
    cutted_list = []
    
    for index in range(0 , len(numbers)) :
        if index >= num1 and index <= num2 :
            cutted_list.append(numbers[index])
    
    return cutted_list