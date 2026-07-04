from functools import reduce

multiplication = lambda a,b : a*b

def listmaker(n):
    arr=list()
    for i in range (n):
        a=int(input("Enter value: "))
        arr.append(a)
    return list(arr)

def main():
    no_elements=int(input("Enter number of elements to insert: "))
    listx=listmaker(no_elements)
    RData=reduce(multiplication,listx)
    print("The product of all elements is :", RData)

if __name__=="__main__":
    main()