import multiprocessing
import time
import os

def summationodd(n):
    print(f"The process id is : {os.getpid()}")
    sum= 0
    for i in range (n+1):
        if i %2 != 0:
            sum = sum+i
    return sum

def main():
    data=[1000000,2000000,3000000,4000000]
    start_time = time.perf_counter()
    pobj1=multiprocessing.Pool()
    result=pobj1.map(summationodd,data)
    pobj1.close()
    pobj1.join()
    end_time = time.perf_counter()

    print(f"The summation of all odd numbers till {data} is {result}")
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ =="__main__":
    main()
    