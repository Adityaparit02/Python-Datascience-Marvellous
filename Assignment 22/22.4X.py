import os
import multiprocessing
import time

def calculate(n):
    sum = 0
    for i in range (n+1):
        sum = sum +(i**5)
    print(f"The process id is : {os.getpid()}")
    return sum

def main():
    data=[1000000,2000000,3000000,4000000]
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(calculate,data)
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"The data was : {data}")
    print(f"The Result is : {result}")
    print(f"Time Taken : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()