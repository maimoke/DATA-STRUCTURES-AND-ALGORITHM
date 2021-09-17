class stack():
    def __init__(self):
        self.value=[]
    def push(self,i):
        self.value.append(i)
    def pop(self):
        temp=self.value[-1]
        self.value.pop(0)
        return temp
    def __str__(self):
        print(self.value,end="")
        return ""
    def isEmpty(self):
        if len(self.value)==0:
            return True
        else :
            return False
class queue():
    def __init__(self):
        self.value=[]
        self.explosiveCounter=0
        self.interrupt=0
    def enqueue(self,i):
        self.value.append(i)
    def dequeue(self):
        temp=self.value[0]
        self.value.pop(0)
        return temp
    def explosionCheckMirror(self,item):
        explosionIndex=999
        while (explosionIndex!=None):
            alp=""
            point=0
            explosionIndex=None
            for i in reversed(range(len(self.value))):
                if self.value[i]==alp:
                    point=point+1
                else :
                    point=1
                    alp=self.value[i]
                if point==3:
                    explosionIndex=i
                    break
            if explosionIndex!=None:
                self.explosiveCounter=self.explosiveCounter+1
                self.value.pop(explosionIndex)
                self.value.pop(explosionIndex)
                self.value.pop(explosionIndex)
                item.enqueue(alp)
    def explosionCheckNormal(self,item):
        explosionIndex=999
        while (explosionIndex!=None):
            alp=""
            point=0
            explosionIndex=None
            for i in range(len(self.value)):
                if self.value[i]==alp:
                    point=point+1
                else :
                    point=1
                    alp=self.value[i]
                if point==3:
                    explosionIndex=i-2
                    break
            if explosionIndex!=None:
                if not item.isEmpty():
                    temp=item.dequeue()
                    self.value.insert(explosionIndex+2,temp)
                    if temp==alp:
                        self.interrupt=self.interrupt+1
                        self.value.pop(explosionIndex)
                        self.value.pop(explosionIndex)
                        self.value.pop(explosionIndex)
                else:
                    self.explosiveCounter=self.explosiveCounter+1
                    self.value.pop(explosionIndex)
                    self.value.pop(explosionIndex)
                    self.value.pop(explosionIndex)
    def isEmpty(self):
        if len(self.value)==0:
            return True
        else :
            return False
    def r(self):
        self.value.reverse()
    def output(self,re):
        if re==0:
            print("NORMAL :")
            print(len(self.value))
            if (len(self.value)!=0):
                for i in self.value:
                    print(i,end="")
                print("")
            else :
                print("Empty")
            print("{} Explosive(s) ! ! ! (NORMAL)".format(self.explosiveCounter))
            if (self.interrupt>0):
                print("Failed Interrupted {} Bomb(s)".format(self.interrupt))
        else:
            print(": RORRIM")
            print(len(self.value))
            if (len(self.value)!=0):
                for i in self.value:
                    print(i,end="")
                print("")
            else :
                print("ytpmE")
            print("(RORRIM) ! ! ! (s)evisolpxE {}".format(self.explosiveCounter))
if __name__=="__main__":
    inp=input("Enter Input (Normal, Mirror) : ").split(" ")
    normal=queue()
    mirror=queue()
    item=queue()
    for i in inp[0]:
        normal.enqueue(i)
    for i in inp[1]:
        mirror.enqueue(i)
    mirror.explosionCheckMirror(item)
    normal.explosionCheckNormal(item)
    normal.r()
    normal.output(0)
    print("------------MIRROR------------")
    mirror.output(1)