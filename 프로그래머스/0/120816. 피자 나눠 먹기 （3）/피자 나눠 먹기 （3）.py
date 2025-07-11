def solution(slice, n):
    pizza_count = 0
    slice2 = slice
    
    if slice >= n :
        pizza_count = 1
        return pizza_count
    elif slice < n :
        pizza_count = 1
        while slice < n :
            slice += slice2
            pizza_count += 1
        
        return pizza_count