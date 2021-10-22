if __name__=="__main__":
    print(" *** Wind classification ***")
    inp=float(input("Enter wind speed (km/h) : "))
    if inp>=209:
        print("Wind classification is Super Typhoon.")
    elif inp>=102:
        print("Wind classification is Typhoon.")
    elif inp>=56:
        print("Wind classification is Tropical Storm.")
    elif inp>=52:
        print("Wind classification is Depression.")
    elif inp>=0:
        print("Wind classification is Breeze.")
    else :
        print("!!!Wrong value can't classify.")