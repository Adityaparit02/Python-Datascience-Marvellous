import multiprocessing
import time
import os

def countevennos(n):
    count = 0
    for i in range(2,n+1):
        if i % 2 == 0:
            count = count+1
    return count

def main():
    no=int(input("Enter number : "))

    start_time = time.perf_counter()

    pobj=multiprocessing.Pool()
    result = pobj.map(countevennos,(no,))
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"The count of even numbers till {no} is {result}")
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ =="__main__":
    main()