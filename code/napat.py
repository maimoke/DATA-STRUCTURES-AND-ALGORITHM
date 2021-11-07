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
        if self.root ==None:
            self.root = Node(data)
            return self.root
        else:
            now=self.root
            while now:
                if data >= now.data:
                    if now.right is None:
                        now.right = Node(data)
                        return self.root
                    else:
                        now=now.right
                elif data < now.data:
                    if now.left is None:
                        now.left = Node(data)
                        return self.root
                    else:
                        now=now.left


    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkBelow(self,node,number,list=[]):
        if node!= None:
            self.checkBelow(node.left,number,list)
            if node.data<number:
                list.append(node.data)
            self.checkBelow(node.right,number,list)
        return list
    def delete(self,node,number):
        pass
T = BST()
inp = [i.split() for i in input("Enter Input : ").split(",")]
for i in inp:
    if i[0] == "i":
        root=T.insert(int(i[1]))
        print("insert {}".format(i[1]))
        T.printTree(root)
    else:
        pass

T.printTree(root)