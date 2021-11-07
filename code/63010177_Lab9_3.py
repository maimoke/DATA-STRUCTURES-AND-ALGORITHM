def metaDrome(s):
    same=[]
    for i in range(len(s)-1):
        if s[i]<=s[i+1] and not repeat(same,s[i]):
            same.append(s[i])
        else:
            return False
    if repeat(same,s[i+1]):
        return False
    return True
        
def plainDrome(s):
    same=[]
    for i in range(len(s)-1):
        if s[i]<=s[i+1]:
            same.append(s[i])
        else:
            return False
    for i in range(len(s)):
        for j in s[i+1:]:
            if s[i] is j:
                return True
    return False
def kataDrome(s):
    same=[]
    for i in range(len(s)-1):
        if s[i]>=s[i+1] and not repeat(same,s[i]):
            same.append(s[i])
        else:
            return False
    return True
def nialpDrome(s):
    same=[]
    for i in range(len(s)-1):
        if s[i]>=s[i+1]:
            same.append(s[i])
        else:
            return False
    for i in range(len(s)):
        for j in s[i+1:]:
            if s[i] is j:
                return True
    return False
def repDrome(s):
    for i in range(len(s)-1):
        if s[i] is not s[i+1]:
            return False
        else:
            return True
def repeat(same,char):
    for i in same:
        if i is char:
            return True
    return False
if __name__=="__main__":
    inp=input("Enter Input : ")
    if repDrome(inp):
        print("Repdrome")
    elif metaDrome(inp):
        print("Metadrome")
    elif plainDrome(inp):
        print("Plaindrome")
    elif kataDrome(inp):
        print("Katadrome")
    elif nialpDrome(inp):
        print("Nialpdrome")
    else:
        print("Nondrome")