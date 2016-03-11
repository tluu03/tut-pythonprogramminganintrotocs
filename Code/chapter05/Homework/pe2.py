#pe2.py
def main():
    grade=input("What is your grade?1-4?")
    if grade=="1":
        grade="A"
    elif grade=="2":
        grade="B"
    elif grade=="3":
        grade="C"
    elif grade=="4":
        grade="F"
    print("Your grade is:",grade)
