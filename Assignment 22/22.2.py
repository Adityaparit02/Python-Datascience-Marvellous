import multiprocessing
import os
import time


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"The process id is : {os.getpid()}")

    return fact

def main():
    data = [10,15,20,25]

    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()
    result=pobj.map(fact,data)
    pobj.close()
    pobj.join

    end_time=time.perf_counter()

    print (f"The factorial is : {result}")
    print(f"Time Required : {end_time-start_time :.4f} seconds")

if __name__ == "__main__":
    main()

