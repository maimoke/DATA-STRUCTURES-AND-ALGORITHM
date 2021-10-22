def rotation(str):
    newstr=str[len(str)-1]
    newstr=newstr+str[0:len(str)-1]
    return newstr
def rotation2(str):
    newstr=str[1:len(str)]
    newstr=newstr+str[0]
    return newstr
if __name__=="__main__":
    print("*** String Rotation ***")
    inp=input("Enter 2 strings : ").split(" ")
    str1=inp[0]
    str2=inp[1]
    round=1
    str1=rotation(str1)
    str2=rotation2(str2)
    while inp[0]!=str1 or inp[1]!=str2:
        if round<=5:
            print("{} {} {}".format(round,str1,str2))
        if round == 6:
            print(" . . . . . ")
        str1=rotation(str1)
        str2=rotation2(str2)
        round=round+1
    print("{} {} {}".format(round,str1,str2))
    print("Total of  {} rounds.".format(round))