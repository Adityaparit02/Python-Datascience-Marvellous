from Library_12 import calculator
def main():
    n=int(input("Enter first number : "))
    n1=int(input("Enter second number :"))
    a,s,m,d=calculator(n,n1)
    print(n,"+",n1,"=",a)
    print(n,"-",n1,"=",s)
    print(n,"x",n1,"=",m)
    print(n,"/",n1,"=",d)

if __name__=="__main__":
    main()