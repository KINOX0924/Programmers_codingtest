def transDecimal(number , length = 15) :
    if length < 15 :
        length = 15
    square_list = [ 2**x for x in range(length) ]
    decimal     = 0
    
    for index , binary in enumerate(number[::-1]) :
        if binary == "1" :
            decimal += square_list[index]
    
    return decimal  # 여기서 반환된 decimal 값의 타입은 int

def transBinary(number , length = 15) :     # 여기서 매개변수로 들어온 number 의 타입은 int
    if length < 15 :
        length = 15
    square_list = [ 2**x for x in range(length) ]
    binary = ""
    
    for square in square_list[::-1] :
        if number >= square :
            binary += "1"
            number -= square
        else :
            binary += "0"
    start = binary.find("1")
    
    return binary[start::]

def solution(bin1, bin2):
    length = 0
    
    if len(bin1) >= len(bin2) :
        length = len(bin1)
    else :
        length = len(bin2)
    
    decimal1 = transDecimal(bin1 , length)
    decimal2 = transDecimal(bin2 , length)
    
    binary = transBinary((decimal1+decimal2) , length)
    
    return binary