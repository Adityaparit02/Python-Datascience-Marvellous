import multiprocessing
import os
import time


def fact(n):
    print(f"Process id is : {os.getpid()}")
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main():
    no=int(input("Enter value : "))

    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()
    result=pobj.map(fact,(no,))
    pobj.close()
    pobj.join

    end_time=time.perf_counter()

    print (f"The factorial is : {result}")
    print(f"Time Required : {end_time-start_time :.4f} seconds")

if __name__ == "__main__":
    main()

