class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        last=self
        while (last.next is not None):
            print(last.data,end=" ")
            last=last.next
        print(last.data,end=" ")
        return ""
def createList(l=[]):
    for i in range(len(l)):
        if i == 0:
            headnode=node(l[i])
            last=headnode
        else :
            newnode=node(l[i])
            last.next=newnode
            last=last.next
    return headnode

def printList(H):
    print(H)

def mergeOrderesList(p,q):
    lastp=p
    lastq=q
    if lastp.data>lastq.data:
        headnode=node(lastq.data)
        lastm=headnode
        lastq=lastq.next
    else :
        headnode=node(lastp.data)
        lastm=headnode
        lastp=lastp.next
    
    while True:
        if lastp is None and lastq is None:
            return headnode
        elif lastp is None:
            newnode=node(lastq.data)
            lastq=lastq.next
            lastm.next=newnode
            lastm=lastm.next
        elif lastq is None:
            newnode=node(lastp.data)
            lastp=lastp.next
            lastm.next=newnode
            lastm=lastm.next
        elif int(lastp.data)>int(lastq.data):
            newnode=node(lastq.data)
            lastq=lastq.next
            lastm.next=newnode
            lastm=lastm.next
        else :
            newnode=node(lastp.data)
            lastp=lastp.next
            lastm.next=newnode
            lastm=lastm.next


if __name__=="__main__":
    inp = input("Enter 2 Lists : ").split(" ")
    L1=inp[0].split(",")
    L2=inp[1].split(",")
    #################### FIX comand ####################   
    # input only a number save in L1,L2
    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ',end='')
    printList(LL1)
    print('LL2 : ',end='')
    printList(LL2)
    m = mergeOrderesList(LL1,LL2)
    print('Merge Result : ',end='')
    printList(m)