class Data:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class hash:
    def __init__(self,size,maxColli,threshold):
        self.size =size
        self.maxColli=maxColli
        self.threshold=threshold
        self.table=[]
        for i in range(size):
            self.table.append(None)
    def __str__(self):
        s=""
        for i in range(self.size):
            s=s+"#"+str(i+1)+"\t"+str(self.table[i])+"\n"
        return s
    def insert(self,value):
        #key
        originalkeySum=value
        colliCounter=0
        keySum=originalkeySum
        checker=int(value*100/self.size)
        while True:
            if self.table[keySum%self.size] is not None:
                colliCounter+=1
                print("collision number {} at {}".format(colliCounter,(keySum%self.size)))
                #collision case
                if colliCounter==self.maxColli:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehash()
                    self.table[keySum%self.size]=Data(value)
                    break
                else:
                    keySum=originalkeySum+colliCounter*colliCounter
                    continue
            #threshold case
            elif checker>=self.threshold:
                print("****** Data over threshold - Rehash !!! ******")
                self.rehash()
                self.table[keySum%self.size]=Data(value)
                break
            else:
                self.table[keySum%self.size]=Data(value)
                break
    def rehash(self):
        temp=self.size
        self.size=self.size*2
        while not self.primeCheck(self.size):
            self.size+=1
            
    def primeCheck(self,num):
        prime = True
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
        return prime
if __name__=="__main__":
    print(" ***** Rehashing *****")
    inp =input("Enter Input : ").split("/")
    size,maxColli,threshold=inp[0].split(" ")
    size=int(size)
    maxColli=int(maxColli)
    threshold=int(threshold)
    inp[1]=inp[1].split(" ")
    h=hash(size,maxColli,threshold)
    print("Initial Table :")
    print(h,end="")
    print("----------------------------------------")
    for i in inp[1]:
        print("Add : {}".format(i))
        h.insert(int(i))
        print(h,end="")
        print("----------------------------------------")
