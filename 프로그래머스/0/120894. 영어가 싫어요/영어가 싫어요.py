def transNumber(string) :
    number_dict = {"zero" : "0" , "one" : "1" , "two" : "2" , "three" : "3" , "four" : "4" , "five" : "5" , "six" : "6" , "seven" : "7" , "eight" : "8" , "nine" : "9"}
    temp        = ""
    total       = ""
    
    for char in string :
        temp += char
        if temp in number_dict.keys() :
            total += number_dict[temp]
            temp = ""
    
    return total

def solution(numbers):                      
    total = transNumber(numbers)
    
    return int(total)