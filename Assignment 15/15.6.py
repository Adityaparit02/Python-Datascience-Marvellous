from functools import reduce

minimun_no= lambda a,b: a if a<b else b

def listmaker(n):
    arr=list()
    for i in range (n):
        a=int(input("Enter value:"))
        arr.append(a)

    return list(arr)

def main():
    no_elements=int(input("Enter number of elements to enter in list: "))
    listx=listmaker(no_elements)
    RData=reduce(minimun_no,listx)
    print("The minimum value in list is :",RData)


if __name__=="__main__":
    main()