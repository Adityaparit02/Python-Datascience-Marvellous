import multiprocessing
import threading
from functools import reduce

addition=lambda n,m : n+m

def factlistmker(n,arr):
    for i in range (1,n+1):
        if n%i==0:
            arr.append(i)

    return list(arr)

def addfactors(arr,result):
    total = reduce(addition,arr)
    result.append(total)

def main():
    no=int(input("Enter number : "))
    listx=list()
    result=list()



    t1=threading.Thread(target=factlistmker,args=(no,listx))
    t1.start()
    t1.join()

    t2=threading.Thread(target=addfactors,args=(listx,result)) 
    t2.start()
    t2.join()

    print(f"Factors of {no} are : {listx}")
    print(f"Addition of all factors of {no} is {result}")

if __name__=="__main__":
    main()