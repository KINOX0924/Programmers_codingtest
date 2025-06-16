def wordChk(spell , word) :
    check_list = []
    for char in spell :
        if char in word :
            check_list.append(True)
        elif char not in word :
            check_list.append(False)
    
    if False in check_list :
        return False
    return True

def solution(spell, dic):
    check_list = []
    
    for word in dic :
        if len(spell) == len(word) :
            check_list.append(wordChk(spell , word))
    
    if True in check_list :
        return 1
    return 2