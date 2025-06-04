from collections import Counter

def solution(a, b, c, d):
    num_list = [a , b , c , d]
    answer   = 0
    
    num_dict    = Counter(num_list)
    sorted_dict = num_dict.most_common()
    keys        = num_dict.keys()
    print(sorted_dict)  # 디버깅
    print(num_dict)     # 디버깅
    
    if len(sorted_dict) == 1 :
        answer = sorted_dict[0][0] * 1111
    elif len(sorted_dict) == 2 and sorted_dict[0][1] == 3 :
        answer = (10 * sorted_dict[0][0] + sorted_dict[1][0])**2
    elif len(sorted_dict) == 2 and sorted_dict[0][1] == 2 :
        answer = (sorted_dict[0][0] + sorted_dict[1][0]) * abs(sorted_dict[0][0] - sorted_dict[1][0])
    elif len(sorted_dict) == 3 :
        answer = sorted_dict[1][0] * sorted_dict[2][0]
    elif len(sorted_dict) == 4 :
        answer = int(min(keys))
    
    return answer