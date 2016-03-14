#pe4.py
#program that makes acronyms
def main():
    phrase = input("enter a phrase:")
    words = phrase.split(" ")
    letters = [i[0].upper()for i in words]
    print("".join(letters))
