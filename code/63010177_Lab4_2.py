class queue():
    def __init__(self,size):
        self.value=[]
        self.size=size
    def q(self,i):
        self.value.append(i)
    def dq(self):
        if len(self.value)!=0:
            temp=self.value[0]
            self.value.pop(0)
            return temp
    def isFull(self):
        return len(self.value)==self.size
    def isEmpty(self):
        if len(self.value)==0:
            return True
        else :
            return False
    def __str__(self):
        temp=str(self.value)
        return temp
if __name__=="__main__":
    q=queue(999)
    cashier1=queue(5)
    cashier2=queue(5)
    inp=input("Enter people : ")
    for i in inp:
        q.q(i)
    minute=0
    c2minute=0
    while not q.isEmpty():
        if (minute%3==0 and minute!=0):
            cashier1.dq()

        if (not cashier2.isEmpty()):
            c2minute=c2minute+1

        if (c2minute%2==0 and minute!=0):
            cashier2.dq()

        if (not cashier1.isFull()):
            cashier1.q(q.dq())
        elif (not cashier2.isFull()):
            cashier2.q(q.dq())

        minute=minute+1
        print(minute,end=" ")
        print(q,end=" ")
        print(cashier1,end=" ")
        print(cashier2,end=" ")
        print("")

        
