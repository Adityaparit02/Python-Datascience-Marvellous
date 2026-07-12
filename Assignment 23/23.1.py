import os
import multiprocessing
import time

def summation(n):
    print(f"Process id : {os.getpid()}")
    sum=0
    for i in range(n+1):
        if i % 2 ==0:
            sum=sum+i

    return sum


def main():
   # no=int(input("Enter Number : "))

    start_time=time.perf_counter()
    data=[1000000,2000000,3000000,4000000]
    pobj=multiprocessing.Pool()
    result=pobj.map(summation,data)
    pobj.close()
    pobj.join

    end_time=time.perf_counter()

    print(f"Time Taken : {end_time-start_time:.4f} seconds")

    print(f"The addition of all even numbers till {data} is {result}")


if __name__=="__main__":
    main()