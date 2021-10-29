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
    def rank(self,node,data):
        if node.right is None and node.left is None:
            if data>=node.data:
                return 1
            else:
                return 0
        elif node.right is None:
            if data>=node.data:
                return self.rank(node.left,data)+1
            else:
                return self.rank(node.left,data)
        elif node.left is None:
            if data>=node.data:
                return self.rank(node.right,data)+1
            else:
                return self.rank(node.right,data)
        else:
            if data>=node.data:
                return self.rank(node.right,data)+self.rank(node.left,data)+1
            else:
                return self.rank(node.right,data)+self.rank(node.left,data)
if __name__=="__main__":
    Tree=BST()
    inp=input("Enter Input : ").split("/")
    ins=[int(i) for i in inp[0].split()]
    check=int(inp[1])
    for i in ins:
        root=Tree.insert(i)
    Tree.printTree(root)
    print("--------------------------------------------------")
    print("Rank of {} : {}".format(check,Tree.rank(root,check)))