import multiprocessing
import time
import os

def sumofpowers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i ** 5)

    print(f"Process ID : {os.getpid()}")
    print(f"Input Number : {n}")
    print(f"Sum of 5th Powers : {total}\n")

    return total

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(sumofpowers, data)
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Results :", result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()