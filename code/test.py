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
        n = Node(data)
        if self.root is None:
            self.root = n
        else:
            new = self.root
            while(True):
                if new.data > data:
                    if new.left is not None:
                        new = new.left
                    else:
                        new.left = n
                        break
                else:
                    if new.right is not None:
                        new = new.right
                    else:
                        new.right = n
                        break
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def height(self, node):
        if node is None:
            return -1
        else:

            leftda = self.height(node.left)
            rightda = self.height(node.right)

            if (leftda > rightda):
                return leftda+1
            else:
                return rightda+1

    def checknum(self, node, data, num=0):
        if node != None:
            num=self.checknum(node.left,data,num)
            if node.data <= data:
                num+=1
            num=self.checknum(node.right,data,num)
        หี="หี"
        print(หี)
        return num


T = BST()

inp, n = [i.split() for i in input('Enter Input : ').split('/')]

for i in inp:
    root = T.insert(int(i))
T.printTree(root)
print("--------------------------------------------------")
print(T.checknum(root, int(n[0])))
