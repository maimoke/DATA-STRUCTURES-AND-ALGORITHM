class Node:
    def __init__(self,name, data):
        self.name = name
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class Stack:
    def __init__(self):
        self.value=[]
    def push(self,data):
        self.value.append(data)
    def pop(self):
        temp=self.value[-1]
        self.value.pop()
        return temp
    def Last(self):
        return len(self.value)-1==0
class Tree:
    def __init__(self):
        self.root = None
        self.height = 0
    def insert(self,name,data):
        s=Stack()
        temp=name
        node=self.root
        if node==None:
            self.root=Node(name,data)
            return self.root
        while (temp!=0):
            if temp%2==1:
                temp=(temp-1)/2
                s.push("R")
            else:
                temp=(temp-2)/2
                s.push("L")
        while not s.Last():
            temp=s.pop()
            if temp=="L":
                node=node.left
            elif temp=="R":
                node=node.right
        temp=s.pop()
        if temp=="L":
            node.left=Node(name,data)
            return self.root
        else:
            node.right=Node(name,data)
            return self.root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def stats(self,node):
        if node.left==None and node.right==None:
            return node.data
        if node.left==None:
            return self.stats(node.right)+node.data
        elif node.right==None:
            return self.stats(node.left)+node.data
        else :
            return self.stats(node.left)+self.stats(node.right)+node.data
    def find(self,name):
        s=Stack()
        temp=name
        node=self.root
        if temp ==0:
            return self.root
        while (temp!=0):
            if temp%2==1:
                temp=(temp-1)/2
                s.push("R")
            else:
                temp=(temp-2)/2
                s.push("L")
        while not s.Last():
            temp=s.pop()
            if temp=="L":
                node=node.left
            elif temp=="R":
                node=node.right
        temp=s.pop()
        if temp=="L":
            return node.left
        else:
            return node.right
    def compare(self,a,b):
        if self.stats(self.find(a))>self.stats(self.find(b)):
            return ">"
        elif self.stats(self.find(a))<self.stats(self.find(b)):
            return "<"
        else:
            return "="
T = Tree()
inp =input("Enter Input : ").split("/")
ins = [int(i) for i in inp[0].split(" ")]
comp = inp[1].split(",")
for i in range(len(ins)):
    root = T.insert(i,ins[i])
print(T.stats(root))
for i in range(len(comp)):
    a,b=comp[i].split(" ")
    a=int(a)
    b=int(b)
    print("{}{}{}".format(a,T.compare(a,b),b))
print()
                
    
