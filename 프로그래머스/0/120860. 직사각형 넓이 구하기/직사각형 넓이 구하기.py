def getWidth(dots) :    
    x     = dots[0][0]
    width = 0
    # print(dots)   # 디버깅
    
    while x != dots[2][0] :
        width += 1
        x += 1
    # print(width)  # 디버깅
    
    return width

def getHeight(dots) :
    y      = dots[0][1]
    height = 0
    
    while y != dots[1][1] :
        height += 1
        y += 1
        
    # print(height)
    
    return height

def solution(dots):
    width  = getWidth(sorted(dots))
    height = getHeight(sorted(dots))

    return width * height