#pe14.py
#make a wc program (word count)
#requirements
#should except file name as input
#print three numbers showing the count of lines
#prints the words and characters in the file
def main():
    print('This program will count words and show the details of each file.\n')
     
    filename = input('Type in the filename: ')
     
    infile = open(filename,'r')
     
    lines,words,chars = 0,0,0
     
    for i in infile:
        lines = lines + 1
        chars = chars + len(i[:-1])
        words = words + len(i.split())
     
    infile.close()
     
    print('"{}" has {} lines, {} words and {} characters.'
          .format(filename,lines,words,chars))        

     


    
