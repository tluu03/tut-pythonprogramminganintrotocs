#pe10.py
#Requirements:
#Algorithm: 
def average(sentence):
    words = sentence.split()
    average = sum(len(word) for word in words)/len(words)

    return average

def main():
    sentence = input("Enter Sentence: ")
    print(average(sentence))




