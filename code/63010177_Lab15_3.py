def gcd(a,b):
    if a==b:
        return a
    if a==0:
        return b
    if b==0:
        return a
    temp=a%b
    if temp==0:
        return b
    if a%temp==0 and b%temp==0:
        return temp
    else:
        return gcd(b,a%b)
inp =input("Enter Input : ").split(" ")
a=int(inp[0])
b=int(inp[1])
if a<0:
    a=0-a
if b<0:
    b=0-b
if a==0 and b==0:
    print("Error! must be not all zero.")
elif int(inp[0])==0 and int(inp[1])<0:
    print("The gcd of {} and {} is : {}".format(inp[0],inp[1],gcd(a,b)))
elif int(inp[1])==0 and int(inp[0])<0:
    print("The gcd of {} and {} is : {}".format(inp[1],inp[0],gcd(a,b)))
elif a>b:
    print("The gcd of {} and {} is : {}".format(inp[0],inp[1],gcd(a,b)))
elif b>a:
    print("The gcd of {} and {} is : {}".format(inp[1],inp[0],gcd(b,a)))
else:
    print("The gcd of {} and {} is : {}".format(inp[1],inp[0],gcd(a,b)))
