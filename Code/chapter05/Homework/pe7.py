#pe7.py
#program that uses a caesar cipher
# Requirements:
# 1) 
def main():
    word = input("Enter the word you want to encode and decode : ")
    key = eval(input("enter the key you want to use : "))
    encode(word, key)
    decode(word, key)
    
def encode(word, key):
    newWord = ''
    for char in word:
        newWord = newWord + (chr(ord(char)+key))
    print("The encoded word is ", newWord)

def decode(word, key):
    newWord = ''
    for char in word:
        newWord = newWord + (chr(ord(char)-key))
    print("The decoded word is ", newWord)
                             

        
        
        
        
        

    
    
