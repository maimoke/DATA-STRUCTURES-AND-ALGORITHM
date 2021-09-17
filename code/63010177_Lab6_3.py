def POWER(a,b):
    if b==0:
        return 1
    if b!=1:
        b=b-1
        return a*POWER(a,b) 
    else:
        return a
if __name__=="__main__":
    inp=input("Enter Input a b : ").split()
    print(POWER(int(inp[0]),int(inp[1])))