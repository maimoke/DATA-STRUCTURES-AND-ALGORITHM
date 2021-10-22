if __name__=="__main__":
    print(" *** Divisible number ***")
    inp=int(input("Enter a positive number : "))
    if inp <=0 :
        print("{} is OUT of range !!!".format(inp))
    else:
        total = 0
        print("Output ==> ",end="")
        for i in range(inp):
            if inp%(i+1)==0:
                print("{} ".format(i+1),end="")
                total=total+1
        print("")
        print("Total ==> {}".format(total))

