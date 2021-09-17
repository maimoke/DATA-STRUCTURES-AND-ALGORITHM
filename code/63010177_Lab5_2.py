class Node:
    def __init__(self,data,next=None,previous=None):
        self.data = data
        self.next = next
        self.previous = previous
class List:
    def __init__(self,head=None):
        self.head=head
        self.tail=head
    def __str__(self):
        last = self.head
        if self.head is None:
            return ""
        temp=str(self.head.data)
        while last.next!=None:
            last=last.next
            temp=temp+"->"+str(last.data)
        return temp
    def str__reverse(self):
        last =self.tail
        if self.tail is None:
            return ""
        temp=str(self.tail.data)
        while last.previous!=None:
            last=last.previous
            temp=temp+"->"+str(last.data)
        return temp
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    def append(self,data):
        node=Node(data)
        last=self.head
        node.next=None
        
        if self.head is None:
            node.previous = None
            self.head = node
            self.tail = node
            return
        
        while last.next is not None:
            last=last.next
        last.next=node
        node.previous=last
        self.tail=node

    def insert(self,index,data):
        last = self.head
        indextemp =index
        if self.isEmpty():
            if index==0:
                print("index = {} and data = {}".format(index,data))
                self.addBefore(data)
                return
            else :
                print("Data cannot be added")
                return
        if index==0:
            print("index = {} and data = {}".format(index,data))
            self.addBefore(data)
            return
        if index<0:
            print("Data cannot be added")
            return
        index=index-1
        while index>0:
            if last is not None:
                    last=last.next
                    index=index-1
            else :
                print("Data cannot be added")
                return
        print("index = {} and data = {}".format(indextemp,data))
        node=Node(data)
        temp=last.next
        last.next=node
        node.next=temp

        node.previous=last
        if node.next is not None:
            node.next.previous=node
        else :
            self.tail=node
    def addBefore(self,data):
        node=Node(data)
        node.next=self.head
        if self.head is not None:
            self.head.previous = node
        else:
            self.tail=node
        self.head=node
    def remove(self,data):
        index=0
        last=self.head
        if last is None:
            print("Not Found!")
            return
        while int(last.data) != int(data):
            if int(last.data) == int(data):
                continue
            last=last.next
            index=index+1
            if last is None:
                print("Not Found!")
                return
        print("removed : {} from index : {}".format(data,index))
        if last.next is None and last.previous is None:
            self.head=None
            self.tail=None
        elif last is self.head:
            last.next.previous=None
            self.head=last.next
        elif last is self.tail:
            self.tail=last.previous
            self.tail.next=None
        else:
            last.previous.next=last.next
            last.next.previous=last.previous
if __name__=="__main__":
    dll=List()
    inp=input("Enter Input : ").split(",")
    for i in inp:
        if i[0]==" ":
            i=i[1:]
        if i[0:2]=="Ab":
            dll.addBefore(i[3:])
        elif i[0]=="A":
            dll.append(i[2:])
        elif i[0]=="I":
            index=""
            j=2
            while i[j]!=":":
                index=index+i[j]
                j=j+1
            j=j+1
            data=""
            tempbool=False
            for j in i:
                if j==":":
                    tempbool=True
                    continue
                if tempbool:
                    data=data+j
            dll.insert(int(index),int(data))
        elif i[0]=="R":
            dll.remove(int(i[2:]))
        print("linked list :",dll)
        print("reverse :",dll.str__reverse())