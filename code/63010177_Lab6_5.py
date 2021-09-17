def asteroid_collision(asts,index):
    if index>=len(asts) or len(asts)==1: 
        return asts
    #check left
    if index>0:
        if asts[index]<0 and asts[index-1]>0:
            if asts[index-1]>0-asts[index]:
                newasts=asts.copy()
                newasts.pop(index)
                return asteroid_collision(newasts,index-1)
            elif asts[index-1]<0-asts[index]:
                newasts=asts.copy()
                newasts.pop(index-1)
                return asteroid_collision(newasts,index-1)
            else:
                newasts=asts.copy()
                newasts.pop(index-1)
                newasts.pop(index-1)
                return asteroid_collision(newasts,index-2)
    #check right
    elif index<len(asts):
        if asts[index]>0 and asts[index+1]<0:
            if asts[index]>0-asts[index+1]:
                newasts=asts.copy()
                newasts.pop(index+1)
                return asteroid_collision(newasts,index)
            elif asts[index]<0-asts[index+1]:
                newasts=asts.copy()
                newasts.pop(index)
                return asteroid_collision(newasts,index)
            else :
                newasts=asts.copy()
                newasts.pop(index)
                newasts.pop(index)
                return asteroid_collision(newasts,index)
    if index<len(asts):
        newasts=asts.copy()
        return asteroid_collision(newasts,index+1)
    else:
        print("end")
        return asts
x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,0))