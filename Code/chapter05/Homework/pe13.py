#pe13.py
#redo any of the problems and make them batch oriented
#meaning they use text files for input and output
def main():
    print('A Batch program to encrypt file "message.txt" \n')
    key = eval(input('Please provide key to encrypt (1-26): '))
 
    infile = open('message.txt','r')
    outfile = open('encrypted.txt','w')
     
    lookup = 'abcdefghijklmnopqrstuvwxyz'*2+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
                 
    pos = ''           
    tempS = ''          
    tempL = []         
    encrypt = ''            
     
    for line in infile:                    
        for word in line.split():   
            for char in word:
                pos = lookup.find(char)+key
                tempS = tempS + lookup[pos]               
                 
            tempL.append(tempS)
             
            tempS = ''
                 
        encrypt = ' '.join(tempL)
        print(encrypt,file=outfile)
 
        tempL = []
     
    infile.close()
    outfile.close()
     
    print('The message was encrypted to "encrypted.txt"')
 
main()
