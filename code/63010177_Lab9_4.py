alphabet=" abcdefghijklmnopqrstuvwxyz"
def f(str):
    for i in str:
        if i in alphabet:
            return i
    return -1
inp=input("Enter Input : ").split(" ")
for i in range(len(inp)):
    for j in range(len(inp)-1-i):
        if f(inp[j])>f(inp[j+1]):
            inp[j],inp[j+1]=inp[j+1],inp[j]
print(*inp)