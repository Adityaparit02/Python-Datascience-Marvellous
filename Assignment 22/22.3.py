import multiprocessing
import time
import os

def countprimes(n):
    count = 0

    for i in range(2, n + 1):
        isprime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isprime = False
                break

        if isprime:
            count += 1
    
    print(f"Process ID : {os.getpid()}")
    print(f"Input Number : {n}")
    print(f"Total Prime Numbers : {count}\n")

    return count

def main():
    data = [10000, 20000, 30000, 40000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(countprimes, data)
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Prime counts :", result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()