def solution(cipher, code):
    decoding_code = ""
    
    for index , char in enumerate(cipher) :
        if (index + 1) % code == 0 :
            decoding_code += char
    
    return decoding_code
            