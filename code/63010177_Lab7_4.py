class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode=Node(data)
        if self.root is None:
            self.root=newnode
        else:
            nownode=self.root
            while (True):
                if newnode.data >nownode.data:
                    if nownode.right is not None:
                        nownode=nownode.right
                    else:
                        nownode.right=newnode
                        break
                else:
                    if nownode.left is not None:
                        nownode=nownode.left
                    else:
                        nownode.left=newnode
                        break
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def preTree(self, node):
        if node != None:
            print(node,end=" ")
            self.preTree(node.left)
            self.preTree(node.right)
    def inTree(self, node):
        if node != None:
            self.inTree(node.left)
            print(node,end=" ")
            self.inTree(node.right)
    def postTree(self, node):
        if node != None:
            self.postTree(node.left)
            self.postTree(node.right)
            print(node,end=" ")
    def height(self,node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1
    def breadth(self,node):
        h = self.height(node)
        for i in range(1, h+1):
            self.levelSearch(node,i)
    def levelSearch(self,node,level):
        if node is None:
            return
        if level == 1:
            print(node.data,end=" ")
        elif level > 1:
            self.levelSearch(node.left,level-1)
            self.levelSearch(node.right,level-1)
            

class Queue():
    def __init__(self):
        self.value=[]
    def enqueue(self,data):
        self.value.append(data)
    def dequeue(self):
        temp=self.value[0]
        self.value.pop(0)
        return temp
T=BST()
q=Queue()
inp=input("Enter Input : ").split(" ")
for i in inp:
    root = T.insert(int(i))
print("Preorder : ",end="")
T.preTree(root)
print("")
print("Inorder : ",end="")
T.inTree(root)
print("")
print("Postorder : ",end="")
T.postTree(root)
print("")
print("Breadth : ",end="")
T.breadth(root)
