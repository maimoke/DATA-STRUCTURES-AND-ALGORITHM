def pantip(k, n, arr, path):#knr remix
    #k=money 20
    #n=iterator
    #arr=20 10 5 5 2 3 20 10
    #path=bought item
    pattern=0
    if k==0:
        print(*path)
        return 1
    elif n>=len(arr):
        return 0
    else:
        pattern+=pantip(k-arr[n],n+1,arr,path+[arr[n]])
        pattern+=pantip(k,n+1,arr,path)
    
    return pattern

inp = input('Enter Input (Money, Product) : ').split('/') #20/20 10 5 5 3 2 20 10
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))