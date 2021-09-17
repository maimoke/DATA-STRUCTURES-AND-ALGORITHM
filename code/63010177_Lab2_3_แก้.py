def newrange(start, stop=None, step=None):
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

if __name__=='__main__':
    print("*** New Range ***")
    stri=input("Enter Input : ")
    l=list(stri.split(" "))
    output="("
    if len(l)==1 :
        for i in newrange(float(l[0])):
            output=output+str(float(i))+", "
    elif len(l)==2 :
        for i in newrange(float(l[0]),float(l[1])):
            output=output+str(float(i))+", "
    elif len(l)==3 :
        for i in newrange(float(l[0]),float(l[1]),float(l[2])):
            output=output+str(round(float(i),5))+", "

    print(output[:-2]+")")