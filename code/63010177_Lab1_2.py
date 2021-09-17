if __name__=='__main__':
    h,w = input("Enter your High and Weight : ").split()
    BMI = float(w)/(float(h)**2)
    if BMI < 18.5 :
        print("Less Weight")
    elif BMI < 23 :
        print("Normal Weight")
    elif BMI < 25 :
        print("More than Normal Weight")
    elif BMI < 30 :
        print("Getting Fat")
    else :
        print("Fat")