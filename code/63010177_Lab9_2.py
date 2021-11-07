inp = input("Enter Input : ").split(" ")
for i in range(len(inp)):
    inp[i]=int(inp[i])
for k in range(len(inp)):
    for i in range(len(inp)-1):
        j=i+1
        end=False
        while inp[j]<0:
            j+=1
            if j>=len(inp):
                end=True
                break
        if end is True:
            continue
        if inp[i]>inp[j]:
            inp[i],inp[j]=inp[j],inp[i]
print(*inp)