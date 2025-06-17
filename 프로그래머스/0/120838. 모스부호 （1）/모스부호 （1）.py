def decryption(morse_string) :
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    word_list = morse_string.split(" ")
    decryption_string = ""
    
    for morse_word in word_list :
        decryption_string += morse[morse_word]
    
    return decryption_string
    
def solution(letter):
    decryption_string = decryption(letter)
    
    return decryption_string