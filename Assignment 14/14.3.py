compare=lambda a,b : a if a>b else b

def main ():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    c=compare(a,b)
    print("The greater number is :" , c)
if __name__=="__main__":
    main()

