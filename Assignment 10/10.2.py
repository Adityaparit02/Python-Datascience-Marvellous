def Nsum(n):
    sum=0

    for i in range(1,n+1):
        sum=sum+i
    return print("sum of natural numbers till",n,"is",sum)

def main():
    a=int(input("Enter your number:"))

    Nsum(a)

if __name__=="__main__":
    main()