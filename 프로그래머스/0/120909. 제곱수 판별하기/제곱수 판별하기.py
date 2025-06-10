def solution(n):
    
    for number in range(1,1001) :
        if n / number == number :
            print(number)
            return 1
    return 2