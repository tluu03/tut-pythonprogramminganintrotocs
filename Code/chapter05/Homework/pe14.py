#pe14.py
#make a wc program (word count)
#requirements
#should except file name as input
#print three numbers showing the count of lines
#prints the words and characters in the file
def main():
    filename = input("Enter filename: ")
    infile = open(filename,'r')
    wordCount = 0
    characterCount = 0
    lineCount = 0

    for line in infile:
        lineCount = lineCount+1
        characterCount = characterCount+1
    len(line)
    wordCount = wordCount + len(line.split())
    infile.close()

    print("Words in file: ",wordCount)
    print("Characters in the file: ",characterCount)
    print("Lines in the file; ",lineCount)
    
