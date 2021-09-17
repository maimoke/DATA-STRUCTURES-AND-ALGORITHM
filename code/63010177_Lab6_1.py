def rec(list,index,max):
    if index <len(list):
        if int(list[index])>max:
            max=int(list[index])
        index+=1
        return rec(list,index,max)
    else:
        return max
    

if __name__=="__main__":
    inp = input("Enter Input : ").split()
    print("Max :",rec(inp,0,-9999999))