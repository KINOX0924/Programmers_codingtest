def solution(id_pw, db):
    login_information = []
    
    for information in db :
        if id_pw[0] == information[0] and id_pw[1] == information[1] :
            login_information.append("login")
        elif id_pw[0] == information[0] and id_pw[1] != information[1] :
            login_information.append("wrong pw")
        else :
            login_information.append("fail")
    
    if "login" in login_information :
        return "login"
    elif "wrong pw" in login_information :
        return "wrong pw"
    else :
        return "fail"