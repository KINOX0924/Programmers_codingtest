def nearCalculator(int_list , number) :
    near_dict = {}
    
    for num in int_list :
        near_dict[num] = abs(number - num)
    print(near_dict)   # 디버깅
    
    return near_dict

def equlFrequency(near_dict) :
    min_near = 0
    for key in near_dict.keys() :
        if min_near == 0 :
            min_near = near_dict[key]
        
        if min_near > near_dict[key] and min_near != 0 :
            min_near = near_dict[key]
    print(min_near)     # 디버깅
    
    return min_near

def nearNum(min_near , near_dict) :
    near_numbers = sorted([ key for key in near_dict.keys() if near_dict[key] == min_near])
    
    return near_numbers[0]

def solution(array, n):
    # 빈도수처럼 딕셔너리로 만들어서 확인(차이값)
    # 차이값만 꺼내서 가장 낮은 Value 를 가진 key 만 가져옴
    # 차이값이 동률일 경우 가장 낮은 key 값을 제출함
    
    if n in array :
        return n
    
    near_dict = nearCalculator(array , n)
    min_near  = equlFrequency(near_dict)
    near_number = nearNum(min_near,near_dict)
    
    return near_number
    