# A 개의 항목에서 B 개만큼을 고르는 경우의 수를 구하는 공식
# A! // B! * (A - B)!

def getFactorial(number) :
    factorial = number
    num       = number
    
    while num > 1 :
        num -= 1
        factorial *= num
    print(factorial)
    
    return factorial

def solution(balls, share):
    if balls == share :
        return 1
    
    A = getFactorial(balls)
    B = getFactorial(share)
    C = getFactorial(balls - share)
    
    return A / (B * C)