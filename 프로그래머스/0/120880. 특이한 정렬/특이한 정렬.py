def distance(num_list , point) :
    distance_list = []
    
    for number in num_list :
        distance_list.append((number , abs(point-number)))
    
    print(distance_list)    # 디버깅
    
    distance_list.sort(key = lambda x : x[0])
    distance_list.sort(key = lambda x : x[1] , reverse = True)
    print(distance_list)    # 디버깅
    
    return distance_list

def solution(numlist, n):
    number_list = []
    
    number_distance = distance(numlist , n)
    
    for number in number_distance[::-1] :
        number_list.append(number[0])
    
    return number_list