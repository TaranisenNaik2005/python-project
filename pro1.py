inp = int(input("Enter a number"))
num = str(inp)
rev = num[::-1]
rint=int(rev)
if inp==rint :
    print ("Your input number and the reverse of your input number are equal")
else :
    print ("Your input number and the reverse of your input number are not equal")