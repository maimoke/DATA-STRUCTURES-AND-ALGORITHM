if __name__=='__main__' :
    stri=input("Enter Your List : ")
    l=list(stri.split(" "))
    output=[]
    if len(l)>2 :
        for i in range(len(l)-2):
            for j in range(i,len(l)-2):
                for k in range(j,len(l)-2):
                    if int(l[i])+int(l[j+1])+int(l[k+2])==0:
                        temp="["+l[i]+", "+l[j+1]+", "+l[k+2]+"]"
                        if temp not in output:
                            output.append(temp)
        print(str(output).translate({39: None}))
    else :
        print("Array Input Length Must More Than 2")