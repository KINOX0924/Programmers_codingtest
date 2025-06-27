def solution(money):
    ice_americano = [0 , 0]
    
    while money >= 5500 :
        money -= 5500
        ice_americano[0] += 1
    
    ice_americano[1] += money
    
    return ice_americano