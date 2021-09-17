alphabet=" abcdefghijklmnopqrstuvwxyz"
def bon(w):
    secretchar=''
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            if w[i]==w[j]:
                secretchar=w[i]
    return alphabet.find(secretchar)*4
if __name__=='__main__':
    secretCode = input("Enter secret code : ")
    print(bon(secretCode))