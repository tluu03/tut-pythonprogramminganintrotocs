#userfile.py
#   Program to create a fileof username in batch mode

def main():
    print("This program creates a file of usernames from a")
    print("files of names.")

    #get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the username go in? ")

    #open the files
    infile = open(infileName, "r")
    outfile = open(outfilename, "w")

    #process each line odf the input file
    for line in infile:
        #get the first and last names from line
        first, last = line.split()
        #create the username
        uname = (first[0]+last[:7]).lower()
        #write it to the output
        print(uname, file=outfile)

    #close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)
    
        
