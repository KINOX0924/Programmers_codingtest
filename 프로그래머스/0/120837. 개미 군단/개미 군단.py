def antAttack(hp) :
    ants_type = { "General" : 5 , "Solider" : 3 , "Worker" : 1 }
    amy_count = [0 , 0 , 0]
    enemy_hp  = hp
    
    while enemy_hp >= 1 :
        if ants_type["General"] <= enemy_hp :
            enemy_hp -= ants_type["General"]
            amy_count[0] += 1
        elif ants_type["Solider"] <= enemy_hp :
            enemy_hp -= ants_type["Solider"]
            amy_count[1] += 1
        else :
            enemy_hp -= ants_type["Worker"]
            amy_count[1] += 1
    
    print(amy_count)    # 디버깅
    
    return amy_count

def solution(hp):
    amy_count = antAttack(hp)
    
    return sum(amy_count)