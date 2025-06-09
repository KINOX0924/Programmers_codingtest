def solution(order):
    sum_price = 0
    
    for keyword in order :
        if "americano" in keyword or "anything" in keyword :
            sum_price += 4500
        elif "cafelatte" in keyword :
            sum_price += 5000
    
    return sum_price
            