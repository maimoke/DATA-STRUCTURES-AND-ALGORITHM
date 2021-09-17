class stack():
    value=[]
    def __init__(self):
        value=[""]
    def push(self,i):
        self.value.append(i)
        print("Add = {} and Size = {}".format(i,len(self.value)))
    def pop(self):
        if len(self.value)==0 :
            print("-1")
        else:
            print("Pop = {} and Index = {}".format(self.value[-1],len(self.value)-1))
            self.value.pop()
    def __str__(self):
        temp="Value in Stack = "
        if len(self.value)==0 :
            temp=temp+"Empty"
        else:
            for i in self.value:
                temp=temp+str(i)+" "

        return temp

if __name__=='__main__' :
    s=stack()
    inp=input("Enter Input : ").split(",")
    for i in range(len(inp)):
        if inp[i][0]=="A":
            s.push(int(inp[i][2:]))
        else:
            s.pop()
    print(s)
    