class Stack():
    def __init__(self):
        self.value=[]
    def __str__(self):
        temp="Data in Stack is : "
        for i in self.value:
            temp=temp+str(i)+" "
        return temp
    def push(self,data):
        self.value.append(data)
    def pop(self):
        temp=self.value[-1]
        self.value.pop()
        return temp
    def isEmpty(self):
        if len(self.value)==0:
            return True
        else :
            return False
    def size(self):
        return len(self.value)
    def peek(self):
        return self.value[-1]
    def bottom(self):
        return self.value[0]
if __name__=="__main__":
    inp=int(input("Enter choice : "))
    if inp==1:
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())
    elif inp==2:
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.isEmpty())
    elif inp==3:
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())