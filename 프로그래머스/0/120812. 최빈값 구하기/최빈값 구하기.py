def getDict(arr) :
    fre_dict = {}
    
    for num in arr :
        if num not in fre_dict :
            fre_dict[num] = 1
        else :
            fre_dict[num] += 1
    
    return fre_dict

def getMaxFre(fre_dict , arr) :
    fre_max = 1
    
    for num in arr :
        if fre_dict[num] > fre_max :
            fre_max = fre_dict[num]
    
    return fre_max

def getMaxNum(fre_dict , fre_max , arr) :
    max_num_list = []
    
    for num in arr :
        if fre_dict[num] == fre_max and num not in max_num_list :
            max_num_list.append(num)
    
    return max_num_list
    
def solution(array):
    if len(array) == 1 :
        return array[0]

    fre_dict = getDict(array)
    fre_max  = getMaxFre(fre_dict , array)
    max_num_list = getMaxNum(fre_dict , fre_max , array)
    
    if len(max_num_list) == 1 :
        return max_num_list[0]
    else :
        return -1