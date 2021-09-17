class tempstack():
    value=[]
    def __init__(self):
        pass
    def push(self,input):
        self.value.append(input)
    def pop(self):
        temp=self.value[-1]
        self.value.pop()
        return temp
    def size(self):
        return len(self.value)
    def dq(self):
        temp=self.value[0]
        self.value.pop(0)
        return temp
    def peek(self):
        return self.value[-1]
class stack():
    value=[]
    def __init__(self):
        value=[""]
    def manageStack(self,input):
        if input[0]=="A":
            print("Add = {}".format(input[2:]))
            self.value.append(input[2:])
        elif input[0]=="P":
            if (len(self.value))==0:
                print("-1")
            else:
                print("Pop = {}".format(self.value[-1]))
                self.value.pop()
        elif input[0]=="D":
            if len(self.value)==0:
                print("-1")
            else:
                temp=tempstack()
                for i in range(len(self.value)):
                    if self.value[i]==input[2:] :
                        print("Delete = {}".format(self.value[i]))
                        temp.push(self.value[i])
                while temp.size()!=0:
                    self.value.remove(temp.pop())
        elif input[0:2]=="LD":
            if len(self.value)==0:
                print("-1")
            else:
                temp=tempstack()
                for i in range(len(self.value)):
                    if int(self.value[i])<int(input[3:]) :
                        temp.push(self.value[i])
                while temp.size()!=0:
                    print("Delete = {} Because {} is less than {}".format(temp.peek(),temp.peek(),input[3:]))
                    self.value.remove(temp.pop())
        elif input[0:2]=="MD":
            if len(self.value)==0:
                print("-1")
            else:
                temp=tempstack()
                for i in range(len(self.value)):
                    if int(self.value[i])>int(input[3:]) :
                        temp.push(self.value[i])
                while temp.size()!=0:
                    print("Delete = {} Because {} is more than {}".format(temp.peek(),temp.peek(),input[3:]))
                    self.value.remove(temp.pop())
    def __str__(self):
        print("Value in Stack = [",end='')
        print(', '.join(self.value),end='')
        return "]"

if __name__=='__main__' :
    s=stack()
    inp=input("Enter Input : ").split(",")
    for i in range(len(inp)):
        s.manageStack(inp[i])
    print(s)
    