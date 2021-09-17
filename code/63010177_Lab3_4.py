class Stack:

    value=[]
    def __init__(self):
        self.value=[]
    def push(self,input):
        self.value.append(input)
    def lookback(self):
        highest=0
        see=0
        for i in reversed(self.value):
            if int(i)>int(highest):
                see=see+1
                highest=i
        print(see)
    
if __name__=='__main__':
    S = Stack()


    inp = input('Enter Input : ').split(',')

    for i in inp:
        if i[0]=="A":
            S.push(i[2:])
        else :
            S.lookback()