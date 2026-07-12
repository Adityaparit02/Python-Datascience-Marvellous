import multiprocessing
import os
import time

def SumOfSquares(No):
    print("Process is running with PID :", os.getpid())

    # Using the mathematical formula
    Sum = (No * (No + 1) * (2 * No + 1)) // 6

    return Sum

def main():

    Data = [1000000000, 2000000000, 3000000000, 4000000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOfSquares, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("\nResult is:")
    print(Result)

    print(f"\nTime Required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()