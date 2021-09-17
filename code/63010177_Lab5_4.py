from typing import NoReturn


class node():
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class StackCalc():
    error=0
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,data):
        if self.head is None:
            headnode=node(data)
            self.head=headnode
            self.tail=headnode
        else:
            newnode=node(data)
            newnode.previous=self.tail
            self.tail=newnode
            
    def pop(self):
        temp=self.tail.data
        self.tail=self.tail.previous
        return temp
    def run(self,input):
        list= input.split()
        for i in list:
            if i=="+":
                self.push(self.pop()+self.pop())
            elif i=="-":
                self.push(self.pop()-self.pop())
            elif i=="*":
                self.push(self.pop()*self.pop())
            elif i=="/":
                self.push(int(self.pop()/self.pop()))
            elif i=="DUP":
                self.push(self.tail.data)
            elif i=="POP":
                self.pop()
            elif i=="PSH":
                pass
            elif i.isnumeric():
                self.push(int(i))
            else:
                print("Invalid instruction: {}".format(i))
                self.error=1
                return
    def getValue(self):
        if self.error==1:
            return ""
        else:
            if self.tail is None:
                return 0
            else:
                return self.tail.data
        





if __name__=="__main__":
    print("* Stack Calculator *")
    arg = input("Enter arguments : ")
    machine = StackCalc()
    machine.run(arg)
    print(machine.getValue())