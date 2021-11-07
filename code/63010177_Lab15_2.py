def c(list,max,i=0):
    if i>=len(list):
        return max
    if int(list[i])>max:
        max=int(list[i])
    max=c(list,max,i+1)
    return max
inp=input("Enter Input : ").split(" ")
print("Max : {}".format(c(inp,-10000)))