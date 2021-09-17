if __name__ == '__main__':
    print ("*** Fun with Drawing ***")
    n=int(input("Enter input : "))
    #line 1
    for i in range(n-1):
        print (".",end='')
    print("*",end='')
    for i in range((n-2)*2+1) :
        print (".",end='')
    print("*",end='')
    for i in range(n-1):
        print (".",end='')
    print("")
    #line 2 - n-1
    for j in range(n-2,0,-1) :
        for i in range(j) :
            print(".",end='')
        print("*",end='')
        for i in range((n-2-j)*2+1) :
            print("+",end='')
        print("*",end='')
        for i in range(j*2-1) :
            print(".",end='')
        print("*",end='')
        for i in range((n-2-j)*2+1) :
            print("+",end='')
        print("*",end='')
        for i in range(j) :
            print(".",end='')
        print("")
    #line n
    print ("*",end='')
    for i in range((n-2)*2+1):
        print("+",end='')
    print ("*",end='')
    for i in range((n-2)*2+1):
        print("+",end='')
    print ("*")
    #line >n
    line=1
    p=(n-2)*4+1
    while (p>0):
        for i in range(line):
            print(".",end='')
        print("*",end='')
        for i in range(p):
            print("+",end='')
        print("*",end='')
        for i in range(line):
            print(".",end='')
        print("")
        p=p-2
        line=line+1
    #last line
    for i in range(line):
        print(".",end='')
    print("*",end='')
    for i in range(line):
        print(".",end='')



    