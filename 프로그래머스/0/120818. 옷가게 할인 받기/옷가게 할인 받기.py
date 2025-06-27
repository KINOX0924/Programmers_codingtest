def solution(price):
    if price < 100000 :
        return price

    sale_price = 0
    
    if price >= 500000 :
        sale_price = price * 0.2
    elif price >= 300000 :
        sale_price = price * 0.1
    elif price >= 100000 :
        sale_price = price * 0.05
    
    return int(price - sale_price)