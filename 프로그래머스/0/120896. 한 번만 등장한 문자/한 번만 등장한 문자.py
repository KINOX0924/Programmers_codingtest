def division(string_type) :
    fre_dict = {}
    for char in string_type :
        if char not in fre_dict.keys() :
            fre_dict[char] = 1
        else :
            fre_dict[char] += 1
            
    return fre_dict

def resultCount(dict_type) :
    result = ""
    
    for key in dict_type :
        if dict_type[key] == 1 :
            result += key
    
    return "".join(sorted(result))
    
def solution(s) :
    char_frequency_dict = division(s)
    result = resultCount(char_frequency_dict)
    
    return result
    