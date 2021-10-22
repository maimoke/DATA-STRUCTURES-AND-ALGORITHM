if __name__=="__main__":
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    lower="abcdefghijklmnopqrstuvwxyz "
    upcheck=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lowcheck=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    up=0
    low=0
    print(" *** String count ***")
    inp=input("Enter message : ")
    for i in inp:
        if (i != " "):
            if i in upper:
                upcheck[upper.find(i)]=1
                up=up+1
            if i in lower:
                lowcheck[lower.find(i)]=1
                low=low+1

    print("No. of Upper case characters : {}".format(up))
    print("Unique Upper case characters :",end="")
    for i in range(len(upcheck)):
        if upcheck[i]==1:
            print(" {} ".format(upper[i]),end="")
    print("")
    print("No. of Lower case Characters : {}".format(low))
    print("Unique Lower case characters :",end="")
    for i in range(len(lowcheck)):
        if lowcheck[i]==1:
            print(" {} ".format(lower[i]),end="")
    