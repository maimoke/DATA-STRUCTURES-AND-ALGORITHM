
#ไม้โมก

class num(object):
    num1=0
    def __init__(self,num1):
        self.num1=num1

    def __add__(self,other):
       return self.num1+other.num1

    def __mul__(self,other):
        return self.num1 *other.num1

if __name__=='__main__':
    a=num(5)
    b=num(6)
    print(a+b)
    print(a*b)