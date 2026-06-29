def ChkGreater(no1,no2):
    if no1>no2:
        print (no1,"is a greater number")
    else :
        print (no2,"is a greater number")

def main():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    ChkGreater(a,b)

if __name__=="__main__":
    main()