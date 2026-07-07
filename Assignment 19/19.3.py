from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter Value {i} : "))
        arr.append(value)

    return arr

def filterfun(n):
    if n>=70 and n<=90:
        return n

mapfun= lambda n : n+10

reducefun= lambda n,m : n*m


def main():
    no_elements=int(input("Enter number of elements to enter in list : "))
    listx= listmaker(no_elements)

    FData=list(filter(filterfun,listx))
    MData=list(map(mapfun,FData))
    RData=reduce(reducefun,MData)

    print(f"The list is {listx}")
    print(f"The list after filter operation is {list(FData)}")
    print(f"The list after map operation is {list(MData)}")
    print(f"The list after reduce operation is {RData}")

if __name__=="__main__":
    main()