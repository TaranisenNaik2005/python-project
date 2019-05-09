print ('%20s' %"Rules")
print ("1. The amount should be a positive integer")
print ("2. the amount should be a multiples of 100")
inp = int(input("\nEnter the amount :"))
if inp>=2000:
    a = int(inp/2000)
    b = inp%2000
    if b>=500:
        c = int(b / 500)
        d = b % 500
        if d >= 100:
            e = int(d / 100)
            f = d % 100
        else:
            e=0
    else:
        e=0
        c=0
elif inp>=500 and inp<2000:
    a = int(inp/500)
    b = inp%500
    if b>=100:
        c = int(b / 100)
        d = b % 100
        e=0
    else:
        e=0
        c=0
elif inp>=100 and inp<500:
    a = int(inp/100)
    b = inp%100
    c=0
    e=0
else :
    print ("Input the amount that is multible of 100")
    a=0
    c=0
    e=0

print ("You get minimum",a+c+e,"notes")
