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
            s += str(p.data)
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
    def reverse(self):
        temp=LinkedList()
        i = len(self)-1
        while i != -1:
            temp.append(self.nodeAt(i))
            i=i-1
        self.head=temp.head
    def Before(self):
        s = 'Before : '
        p = self.head
        while p.next != None :
            s += str(p.data)+' <- '
            p = p.next
        s += str(p.data)
        return s
    def After(self):
        s = 'After : '
        p = self.head
        while p.data != '0' :
            p = p.next
        s += str(p.data)
        p = p.next
        if p is None:
            p = self.head
        while p.next.data != '0' :
            if p.data =='0':
                return s
            s += ' <- '+str (p.data)
            p = p.next
            if p.next is None:
                s += ' <- ' + str(p.data)
                p = self.head
        s += ' <- '+ str (p.data)
        return s

if __name__=="__main__":
    print(" *** Re order ***")
    inp=input("Enter Input : ").split(" ")
    ll = LinkedList()
    for i in inp:
        ll.append(i)
    print(ll.Before())
    print(ll.After())