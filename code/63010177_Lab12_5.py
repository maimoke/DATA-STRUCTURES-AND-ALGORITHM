class MyInt():
    def __init__(self,value):
        self.value=value
    def __add__(self,another):
        output=self.value+another.value
        output=output*1.5
        print(self.value,end="")
        print(" + ",end="")
        print(another.value,end="")
        print(" = ",end="")
        return int(output)
    def toRoman(self):
        tempvalue=self.value
        roman=""
        while tempvalue != 0:
            if tempvalue>=1000:
                roman=roman+"M"
                tempvalue=tempvalue-1000
            elif tempvalue>=900:
                roman=roman+"CM"
                tempvalue=tempvalue-900
            elif tempvalue>=500:
                roman=roman+"D"
                tempvalue=tempvalue-500
            elif tempvalue>=400:
                roman=roman+"CD"
                tempvalue=tempvalue-400
            elif tempvalue>=100:
                roman=roman+"C"
                tempvalue=tempvalue-100
            elif tempvalue>=90:
                roman=roman+"XC"
                tempvalue=tempvalue-90
            elif tempvalue>=50:
                roman=roman+"L"
                tempvalue=tempvalue-50
            elif tempvalue>=40:
                roman=roman+"XL"
                tempvalue=tempvalue-40
            elif tempvalue>=10:
                roman=roman+"X"
                tempvalue=tempvalue-10
            elif tempvalue>=9:
                roman=roman+"IX"
                tempvalue=tempvalue-9
            elif tempvalue>=5:
                roman=roman+"V"
                tempvalue=tempvalue-5
            elif tempvalue>=4:
                roman=roman+"IV"
                tempvalue=tempvalue-4
            elif tempvalue>=1:
                roman=roman+"I"
                tempvalue=tempvalue-1
        output=str(self.value)+" convert to Roman : "+roman
        return output
        
if __name__=="__main__":
    print(" *** class MyInt ***")
    inp=input("Enter 2 number : ").split(" ")


    a = MyInt(int(inp[0]))

    b = MyInt(int(inp[1]))

    print(a.toRoman())

    print(b.toRoman())

    print(a+b)