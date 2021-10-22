class Queue:
    def __init__(self):
        self.value=[]
    def E(self,data):
        self.value.append(data)
    def D(self):
        self.value.pop(0)
    def isDup(self):
        Dup = False
        for i in range(len(self.value)):
            for j in range(len(self.value)-i-1):
                if self.value[i] == self.value[i+j+1]:
                    Dup=True
        if Dup is True:
            return "Duplicate"
        else:
            return "NO Duplicate"
if __name__=="__main__":
    q=Queue()
    inp=input("Enter Input : ").split("/")
    for i in inp[0].split(" "):
        q.E(i)
    for i in inp[1].split(","):
        if i[0]=='E':
            q.E(i[2:])
        elif i[0]=='D':
            q.D()
    print(q.isDup())



