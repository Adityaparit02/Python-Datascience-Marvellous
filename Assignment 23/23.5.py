import multiprocessing
import time
import os

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print(f"Process ID : {os.getpid()}")
    print(f"Input Number : {n}")
    print(f"Factorial : {fact}\n")

    return fact

def main():
    data = [10, 15, 20, 25]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(factorial, data)
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Factorials are :", result)
    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()