from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter Value {i} : "))
        arr.append(value)
    return arr

def prime_sort(n):
    if n <= 1:
        return None

    for i in range(2, n):
        if n % i == 0:
            return None

    return n

mult_by_2 = lambda n: n*2

max_check = lambda m,n : m if m>n else n

def main():
    no_elements=int(input("Enter number of elements to insert in list : "))
    listx=listmaker(no_elements)

    FData=list(filter(prime_sort,listx))
    MData=list(map(mult_by_2,FData))
    RData=reduce(max_check,MData)

    print(f"The list is : {listx}")
    print(f"The list after filter is : {FData}")
    print(f"The list after map  is : {MData}")
    print(f"The list after reduce is : {RData}")

if __name__=="__main__":
    main()
