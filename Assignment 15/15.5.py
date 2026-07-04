from functools import reduce

maximumlist= lambda a ,b : a if a>b else b

def listmaker(n):
    arr= list()
    for i in range(n):
        a=int(input("Enter value: "))
        arr.append(a)

    return list(arr)


def main():
    no_elements= int(input("Enter no of values to add in list :"))
    listx=listmaker(no_elements)
    RData= reduce(maximumlist,listx)
    print("Maximum in list is:",RData)


if __name__=="__main__":
    main()