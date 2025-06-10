def solution(my_string):
    lists = my_string.split(" ")
    oper_stack = None
    stack = []
    total = 0
    
    for word in lists :
        if word.isdigit() and len(stack) == 0 :
            stack.append(int(word))
        elif word.isdigit() and len(stack) == 1 :
            total = stack.pop()
            if oper_stack == "+" :
                total += int(word)
            else :
                total -= int(word)
            stack.append(total)
            oper_stack = None
        else :
            oper_stack = word
    
    return total