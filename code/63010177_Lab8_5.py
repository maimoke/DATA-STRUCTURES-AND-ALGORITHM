class Node:

    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 



    def __str__(self):

        return str(self.data) 



class Tree:

    def __init__(self): 

        self.root = None

        self.num = 0



    def insert(self, val):  

        if self.root == None:

            self.root = Node(val)

            self.num += 1

        else:

            h = height(self.root)

            max_node = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_node:

                while(current.left != None):

                    current = current.left

                current.left = Node(val)

                self.num+=1

            elif self.num+1 == max_node:

                while(current.right != None):

                    current = current.right

                current.right = Node(val)

                self.num+=1

            else:

                #print(max_node-((max_node-(pow(2,h)-1))/2))

                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val)

                self.num+=1

                    

def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)

            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)

            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)



def check_binary_search_tree_(root,ignore=[]):
    for i in range(len(ignore)):
        for j in range(len(ignore)-i-1):
            if ignore[i]==ignore[j+i+1]:
                return False
    ignore.append(root.data)
    if root.left and root.right is not None:
        if root.right.data > root.data and root.left.data < root.data and root.data>=0 and root.data<=100:
            return check_binary_search_tree_(root.left,ignore) and check_binary_search_tree_(root.right,ignore) and True
        else:
            return False
    elif root.left is not None:
        if root.left.data < root.data and root.data>=0 and root.data<=100:
            return check_binary_search_tree_(root.left,ignore) and True
        else :
            return False
    elif root.right is not None:
        if root.right.data > root.data and root.data>=0 and root.data<=100:
            return check_binary_search_tree_(root.right,ignore) and True
        else:
            return False
    else:
        if root.data>=0 and root.data<=100:
            return True
        else :
            return False

tree = Tree()

data = input("Enter Input : ").split()

for e in data:

    tree.insert(int(e))

printTree90(tree.root)

print(check_binary_search_tree_(tree.root))