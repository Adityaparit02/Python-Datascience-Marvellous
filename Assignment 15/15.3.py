checkodd = lambda n : n%2 != 0

def listmaker(n):
    arr=list()
    for i in range (n):
        b=int(input("Enter value: "))
        arr.append(b)

    return list(arr)

def main():
    no_elements= int (input("Enter number of values to add in list : "))
    c=listmaker(no_elements)
    FData=filter(checkodd,c)
    print("List of odd numbers is :",list(FData))

if __name__=="__main__":
    main()

