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
    def Lowest(self,node):
        if node.left != None:
            return self.Lowest(node.left)
        else:
            return node.data
    def LessThanOrEqual(self,node,k):
        if node == None:
            return 0
        if node.data > k :
            return self.LessThanOrEqual(node.left,k)
        elif node.data <= k:
            return self.LessThanOrEqual(node.right,k)+self.LessThanOrEqual(node.left,k)+1
T=BST()
inp=input("Enter Input : ").split("/")
ins=[int(i) for i in inp[0].split()]
k=int(inp[1])
for i in ins:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.LessThanOrEqual(root,k))