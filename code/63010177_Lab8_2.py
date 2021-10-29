class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 

    def __init__(self):
        self.root = None

    def leftRotate(self, z):
 
        y = z.right
        x = y.left
        # Rotate
        y.left = z
        z.right = x
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        x = y.right
        # Rotate
        y.right = z
        z.left = x
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def getBalance(self, root): #return -1 if right>left return 1 if right<left return 0 if balance 
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def insert(self,root,data):
        #BST Recursion
        if not root: #insert
            return TreeNode(data)

        elif int(data) < int(root.val):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        #Height update (every node in recursion)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and int(data) < int(root.left.val):
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)
 
        if balance < -1 and int(data) > int(root.right.val):
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)

        if balance > 1 and int(data) > int(root.left.val):
            print("Not Balance, Rebalance!")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and int(data) < int(root.right.val):
            print("Not Balance, Rebalance!")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")