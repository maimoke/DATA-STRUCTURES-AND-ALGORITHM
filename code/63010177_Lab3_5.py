class Stack :

    value=[]
    def __init__(self):
        self.value=[]
    def push(self,input):
        self.value.append(input)
    def pop(self):
        temp=self.value[-1]
        self.value.pop()
        return temp
    def size(self):
        return len(self.value)
def dec2bin(decnum):

    s = Stack()
    while decnum!=0:
        s.push(decnum%2)
        decnum=int(decnum/2)
    temp=""
    for i in range(s.size()):
        poptemp=s.pop()
        temp=temp+str(poptemp)
    return temp

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))