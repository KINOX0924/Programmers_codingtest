str = input()

word_list = []

for word in str :
    if ord(word) > 90 :
        word_list.append(chr(ord(word)-32))
    else :
        word_list.append(chr(ord(word)+32))

str = "".join(word_list)
        
print(str)