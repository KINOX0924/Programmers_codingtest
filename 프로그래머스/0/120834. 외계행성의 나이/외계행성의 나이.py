def solution(age):
    alien_age = {"0" : "a" , "1" : "b" , "2" : "c" , "3" : "d" , "4" : "e" , "5" : "f" , "6" : "g" , "7" : "h" , "8" : "i" , "9" :"j"}
    mu_sseuk_answer = ""
    
    for num in str(age) :
        mu_sseuk_answer += alien_age[num]
    
    # print(mu_sseuk_answer)  # Debug
    
    return mu_sseuk_answer