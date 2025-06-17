def getNumber(string) :
    temp = ""
    num_list = []
    
    for char in string :
        if char.isdigit() :
            temp += char
        elif char.isdigit() == False and temp != "":
            num_list.append(int(temp))
            temp = ""
    
    if temp.isdigit() :
        num_list.append(int(temp))
        
    return num_list

def solution(my_string):
    num_list = getNumber(my_string)
    
    print(num_list) # 디버깅
    
    return sum(num_list)