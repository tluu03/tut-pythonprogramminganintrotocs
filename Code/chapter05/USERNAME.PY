#username.py
#simple string processing program to generate usernames

def main():
    print("This program generates computer usernames.\n")

    #get users first and laast names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    #concatanate first initial with 7 chars of the last name
    uname = first[0] + last[:7]

    #output username
    print("Your username is:", uname)
    
