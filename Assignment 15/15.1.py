square= lambda n : n*n

def listmaker(n):
        arr= list()
        for i in range(n):
            a= int (input("Enter value: "))
            arr.append(a)
        return list(arr)


def main():
    a= int(input("Enter the number of elements to be added in list : "))
    c=listmaker(a)
    multarr=map(square,c)
    print("Square of list :",list(multarr))


if __name__=="__main__":
    main()