checkeven = lambda n : n%2==0


def listmaker(n):
    arr=list()
    for i in range (n):
        a=int(input("Enter value :"))
        arr.append(a)
    return list(arr)
def main():
    no_elements = int(input("Enter number of elements to add in list : "))
    a= listmaker(no_elements)
    FData = filter (checkeven,a)
    print("List of even no is :",list(FData))

if __name__=="__main__":
    main()