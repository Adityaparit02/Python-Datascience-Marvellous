import threading
from functools import reduce

addition = lambda n,m : n+m

def evenfactors(n):
    arr=list()
    for i in range(2,n+1):
        if i % 2 == 0 and n % i ==0:
            arr.append(i)

    print(f"The list of  even factors of {n} is {list(arr)}")

    RData=reduce(addition,list(arr))
    print(f"The addition of all even factors is : {RData}")


def oddfactors(n):
    arr=list()
    for i in range (1,n+1):
        if i%2 != 0 and n % i ==0:
            arr.append(i)

    print(f"The list of odd factors of {n} is {list(arr)}")

    RData=reduce(addition,list(arr))
    print(f"The addition of all odd factors is : {RData}")


def main():
    no=int(input("Enter your NUmber : "))

    t1=threading.Thread(target=evenfactors,args=(no,))
    t2=threading.Thread(target=oddfactors,args=(no,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()

