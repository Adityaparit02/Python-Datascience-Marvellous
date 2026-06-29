even=lambda n : (n%2==0)

def listmaker(n):
    a=list()
    for i in range (1,n+1):
        a.append(i)
    return list(a)

def main():
    b=int(input("Enter your number: "))
    c=listmaker(b)
    FData= list(filter(even,c))
    print("List of even numbers till",b,"is",FData)

if __name__=="__main__":
    main()
    