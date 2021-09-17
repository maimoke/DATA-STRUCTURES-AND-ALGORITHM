def weirdSubtract(n,k):
    result = n
    for i in range(k):
        if result%10==0:
            result=result/10
        else:
            result=result -1
    return int(result)
	
if __name__=='__main__' :
    n,s = input("Enter num and sub : ").split()

    print(weirdSubtract(int(n),int(s)))