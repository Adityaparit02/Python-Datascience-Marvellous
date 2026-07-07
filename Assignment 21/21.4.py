import threading
from functools import reduce


def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter value {i} :"))
        arr.append(value)

    return arr


def sum(n):
    sum=0
    for value in n:
        sum=sum+value
    print(f"Sum of the values in list is : {sum}")


def product(n):
    mult=1
    for value in n:
        mult=mult*value

    print(f"Product of the values in list is : {mult}")



def main():
    no_elements=int(input("Enter number of elements to insert in list : "))
    listx=listmaker(no_elements)

    t1=threading.Thread(target=sum,args=(list(listx),))
    t2=threading.Thread(target=product,args=(list(listx),))

    t1.start()
    t2.start()


if __name__=="__main__":
    main()