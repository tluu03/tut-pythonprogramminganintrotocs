#month.py
# a program to print the abbreviation of a month, given its number

def main():
    #months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = eval(input("Enter a month number (1-12): "))

    # compute starting position of a month n in months
    pos = (n-1) * 3

    #Grab the appropriate slice from months

    monthAbbrev = months[pos:pos+3]

    #print the result
    print("The month abbreviation is", monthAbbrev + ".")
          
