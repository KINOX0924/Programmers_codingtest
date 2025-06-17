def solution(box, n):
    x = 0
    x_count = 0
    y = 0
    y_count = 0
    z = 0
    z_count = 0
    
    while x < box[0] :
        if x + n <= box[0] :
            x += n
            x_count += 1
        elif x + n > box[0] :
            break
    
    while y < box[1] :
        if y + n <= box[1] :
            y += n
            y_count += 1
        elif y + n > box[1] :
            break
            
    while z < box[2] :
        if z + n <= box[2] :
            z += n
            z_count += 1
        elif z + n > box[2] :
            break
    
    return x_count * y_count * z_count