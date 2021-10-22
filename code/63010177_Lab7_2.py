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
        if self.root is None:
            self.root=Node(data)
        else:
            nownode=self.root
            while (True):
                if data >nownode.data:
                    if nownode.right is not None:
                        nownode=nownode.right
                    else:
                        nownode.right=Node(data)
                        break
                else:
                    if nownode.left is not None:
                        nownode=nownode.left
                    else:
                        nownode.left=Node(data)
                        break
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def below(self,node,check):
        if node != None:
            self.below(node.left,check)
            if node.data<check:
                print(node.data,end=" ")
            self.below(node.right,check)
    def checkHaveBelow(self,node,check):
        if node.left != None:
            return self.checkHaveBelow(node.left,check)
        else:
            return node.data < check
T = BST()
inp = input("Enter Input : ").split("|")
ins = inp[0].split(" ")
for i in ins:
    root = T.insert(int(i))
T.printTree(root)
print("--------------------------------------------------")
print("Below {} : ".format(int(inp[1])),end="")
if not T.checkHaveBelow(root,int(inp[1])):
    print("Not have")
T.below(root,int(inp[1]))