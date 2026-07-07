import threading
from functools import reduce

addition= lambda n,m : n+m

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter the {i} value for the list: "))
        arr.append(value)

    return list(arr)

def EvenList(n):
    even_data=list()
    for value in n:
        if value % 2 == 0:
            even_data.append(value)

    print(f"The even values in the list are : {even_data}")

    RData=reduce(addition,even_data)
    print(f"The addition of even data is : {RData}")

def OddList(n):
    odd_data=list()
    for value in n:
        if value % 2 != 0:
            odd_data.append(value)

    print(f"The odd values in list are : {odd_data}")

    RData=reduce(addition,odd_data)
    print(f"The addition of odd data is : {RData}")


def main():
    no_elements=int(input("Enter number of elements to be inserted in list : "))
    listx = listmaker(no_elements)
    print(f"The list is : {listx}")
    t1=threading.Thread(target=EvenList,args=(list(listx),))
    t2=threading.Thread(target=OddList,args=(list(listx),))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()





