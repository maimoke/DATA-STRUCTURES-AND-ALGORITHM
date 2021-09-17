al=" abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Queue():
    def __init__(self,value=None):
        self.value=[]
        if value!=None:
            for i in value:
                if i!=" ":
                    self.value.append(i)
    def find(self):
        return al.find(self.value[0])
    def q(self,i):
        self.value.append(i)
        return i
    def dq(self):
        if len(self.value)!=0:
            temp=self.value[0]
            self.value.pop(0)
            return temp
    def isEmpty(self):
        if len(self.value)==0:
            return True
        else :
            return False
    def len(self):
        return len(self.value)
    def __str__(self):
        temp=str(self.value)
        return temp
        
def encodemsg(q1,q2):
    tq2=Queue()
    for i in range(q2.len()):
        tq2.q(q2.q(q2.dq()))
    for i in range(q1.len()):
        temp=q1.find()
        if (temp<=26):
            temp=temp+int(tq2.q(tq2.dq()))
            if (temp>26):
                temp=temp%26
        else :
            temp=temp-26
            temp=temp+int(tq2.q(tq2.dq()))
            if (temp>26):
                temp=temp%26
            temp=temp+26
        temp=al[temp]
        q1.dq()
        q1.q(temp)
    print("Encode message is :  ",end="")
    print(q1)
def decodemsg(q1,q2):
    tq2=Queue()
    for i in range(q2.len()):
        tq2.q(q2.q(q2.dq()))
    for i in range(q1.len()):
        temp=q1.find()
        if (temp<=26):
            temp=temp-int(tq2.q(tq2.dq()))
            if (temp<=0):
                temp=temp+26
        else :
            temp=temp-26
            temp=temp-int(tq2.q(tq2.dq()))
            if (temp<=0):
                temp=temp+26
            temp=temp+26
        temp=al[temp]
        q1.dq()
        q1.q(temp)
    print("Decode message is :  ",end="")
    print(q1)
if __name__=='__main__':
    inp=input("Enter String and Code : ").split(",")
    string=inp[0]
    number=inp[1]
    q1 = Queue(string)
    q2 = Queue(number)
    encodemsg(q1, q2)
    decodemsg(q1, q2)


