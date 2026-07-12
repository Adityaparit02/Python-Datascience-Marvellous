import multiprocessing
import time
import os

def countoddnos(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            count = count+1
    print(f"The process id is : {os.getpid()}")

    return count

def main():
    data = [1000000,2000000,3000000,4000000]
    start_time = time.perf_counter()

    pobj=multiprocessing.Pool()
    result = pobj.map(countoddnos,data)
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"The count of odd numbers till {data} is {result}")
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ =="__main__":
    main()