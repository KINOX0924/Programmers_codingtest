from itertools import combinations , permutations

def printArray(list) :
    for line in list :
        print(line , end = "\n")

def calParallel(list) :
    for line in list :
        if (line[1][1] - line[0][1])*(line[3][0] - line[2][0]) == (line[3][1] - line[2][1]) * (line[1][0] - line[0][0]) :
            return 1
    
    return 0

def solution(dots) :
    index_list = list(permutations(dots , 4))
    # printArray(index_list)
    
    result = calParallel(index_list)
    # print(result)

    return result