class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p
class Queue(LinkedList):
    def enQueue(self,data):
        self.append(data)
    def deQueue(self):
        temp=self.nodeAt(0)
        self.removeHead()
        return temp
    def __str__(self) :
        s = 'Queue data : '
        p = self.head
        if p is None:
            return "Empty Queue"
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s
if __name__=="__main__":
    inp=int(input("Enter choice : "))
    if inp==1:
        q1 = Queue()
        q1.enQueue(10)
        q1.enQueue(20)
        q1.enQueue(30)
        print(q1)
        q1.deQueue()
        q1.enQueue(40)
        print("Size of Queue :",len(q1))
        print(q1)
    elif inp==2:
        q1 = Queue()
        q1.enQueue(100)
        q1.enQueue(200)
        q1.enQueue(300)
        q1.deQueue()
        print(q1)
        print("Queue is Empty :",q1.isEmpty())
    elif inp==3:
        q1 = Queue()
        q1.enQueue(11)
        q1.enQueue(22)
        q1.enQueue(33)
        q1.deQueue()
        q1.deQueue()
        q1.deQueue()
        print(q1)
        print("Size of Queue :",len(q1))
        print("Queue is Empty :",q1.isEmpty())