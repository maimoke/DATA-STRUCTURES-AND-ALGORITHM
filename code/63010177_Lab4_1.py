class queue():
    value=[]
    def __init__(self):
        pass
    def q(self,i):
        self.value.append(i)
        print(len(self.value))
    def dq(self):
        if len(self.value)!=0:
            temp=self.value[0]
            self.value.pop(0)
            return temp+" 0"
        else :
            return -1
    def __str__(self):
        temp=""
        if len(self.value)!=0:
            for i in self.value:
                temp=temp+i+" "
        else:
            temp=temp+"Empty"
        return temp
if __name__=='__main__':
    q=queue()
    inp=input("Enter Input : ").split(",")
    for i in inp:
        if i[0]=="E":
            q.q(i[2:])
        else:
            print(q.dq())
    print(q)
        