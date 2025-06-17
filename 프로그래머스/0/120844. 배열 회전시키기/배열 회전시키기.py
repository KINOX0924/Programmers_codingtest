def solution(numbers, direction):
    temp_list = []
    
    if direction == "right" :
        temp_list.append(numbers.pop())
        temp_list += numbers
        return temp_list
    elif direction == "left" :
        temp_list.append(numbers.pop(0))
        numbers += temp_list
        return numbers