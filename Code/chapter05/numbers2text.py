#numbers2text.py
def main():
    print("this program converts a sequence of unicode numbers into")
    print("the string of text that it represents,\n")

    inString = input("Please enter the governmental coded message: ")

    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)
        message = message + chr(codeNum)

    print("\nThe decoded message is:",message)
