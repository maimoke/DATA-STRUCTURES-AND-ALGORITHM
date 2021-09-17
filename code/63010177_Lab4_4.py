class queue():
    def __init__(self):
        self.value=[]
    def eq(self,i):
        self.value.append(i)
    def dq(self):
        return self.value.pop(0)
    def __str__(self):
        print(', '.join(self.value),end='')
        return ""
    def len(self):
        return len(self.value)
    def translate(self):
        temp=""
        for i in self.value:
            
            if i[0]=="0":
                temp=temp+"Eat"
            elif i[0]=="1":
                temp=temp+"Game"
            elif i[0]=="2":
                temp=temp+"Learn"
            elif i[0]=="3":
                temp=temp+"Movie"

            temp=temp+":"

            if i[2]=="0":
                temp=temp+"Res."
            elif i[2]=="1":
                temp=temp+"ClassR."
            elif i[2]=="2":
                temp=temp+"SuperM."
            elif i[2]=="3":
                temp=temp+"Home"
            temp=temp+", "
        temp=temp[:-2]
        return temp
if __name__=='__main__':
    mq=queue()
    yq=queue()
    inp=input("Enter Input : ").split(",")
    for i in inp:
        mq.eq(i[:3])
        yq.eq(i[4:])
    print("My   Queue = ",end="")
    print(mq)
    print("Your Queue = ",end="")
    print(yq)
    print("My   Activity:Location = ",end="")
    print(mq.translate())
    print("Your Activity:Location = ",end="")
    print(yq.translate())
    score=0
    for i in range(mq.len()):
        me=mq.dq()
        you=yq.dq()
        if (me[:1]==you[:1] and me[-1:]==you[-1:]):
            score=score+4
        elif (me[:1]==you[:1] and me[-1:]!=you[-1:]):
            score=score+1
        elif (me[:1]!=you[:1] and me[-1:]==you[-1:]):
            score=score+2
        else:
            score=score-5
    
    if (score>=7):
        print("Yes! You're my love! : Score is ",end="")
        print(score,end="")
        print(".")
    elif (score>0):
        print("Umm.. It's complicated relationship! : Score is ",end="")
        print(score,end="")
        print(".")
    else:
        print("No! We're just friends. : Score is ",end="")
        print(score,end="")
        print(".")