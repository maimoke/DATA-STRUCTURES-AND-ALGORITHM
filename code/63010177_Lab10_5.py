def recur(list,box,now=[],n=0,start=False,ans=[]):
    if start is False:
        for i in range(box):
            now.append([])
    if n==len(list):
        print(*now)
        highest=0
        for i in range(box):
            sum=0
            for j in range(len(now[i])):
                sum+=now[i][j]
            if highest<sum:
                highest=sum
        return highest
    for i in range(box):
        now[i].append(list[n])
        ans.append(recur(list,box,now,n+1,True,ans))
        now[i].remove(list[n])
    if n==0:
        return ans
    else:
        return 9999
if __name__=="__main__":
    inp=input("Enter Input : ").split("/")
    list=[]
    for i in inp[0].split(" "):
        list.append(int(i))
    box=int(inp[1])
    minimum=999
    for i in recur(list,box):
        if i<minimum:
            minimum=i
    print(minimum)