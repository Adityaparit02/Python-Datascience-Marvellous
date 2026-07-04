comparesmall= lambda a,b : a if a<b else b

def main():
    a=int (input("Enter first number :"))
    b=int (input("Enter second number :"))
    c=comparesmall(a,b)
    print ("The smallest number is :",c)

if __name__=="__main__":
    main()