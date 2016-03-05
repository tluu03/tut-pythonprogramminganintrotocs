#text2numbers.py
#    a program to convert a textual message into a sequence of
#       numbers, utilizing the underlying unicode encoding.

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the unicode encoding of the message.\n")

    #get the message to encode
    message = input("please enter the message to encode: ")
    print("\nHere are the top secret governmental codes:")
    #loop through the message and print out unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print() # blank line before prompt
    
