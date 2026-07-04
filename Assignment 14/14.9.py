multiplication= lambda a,b: a*b

def main():
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    c=multiplication(a,b)
    print("Multiplication is:", c)

if __name__=="__main__":
    main()