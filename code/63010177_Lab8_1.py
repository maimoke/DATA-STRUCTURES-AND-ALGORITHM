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

    def insert(self, data,node=None):
        if self.root is None:
            print("*")
            self.root=Node(data)
        else:
            if node is None:
                node=self.root
            if data >= node.data:
                return self.R(data,node)
            else:
                return self.L(data,node)

    def R(self,data,node):
        if node.right is None:
            print("R*")
            node.right=Node(data)
        else:
            print("R",end="")
            return self.insert(data,node.right)
    
    def L(self,data,node):
        if node.left is None:
            print("L*")
            node.left=Node(data)
        else:
            print("L",end="")
            return self.insert(data,node.left)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
if __name__=="__main__":
    Tree=BST()
    inp=input("Enter Input : ").split(" ")
    for i in inp:
        Tree.insert(int(i))