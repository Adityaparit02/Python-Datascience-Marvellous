import MarvellousNum

def ListPrime(arr):
    total = 0
    prime_list = []

    for no in arr:
        if MarvellousNum.ChkPrime(no):
            prime_list.append(no)
            total = total + no

    return prime_list, total


def main():
    size = int(input("Enter number of elements: "))

    arr = []

    for i in range(size):
        no = int(input("Enter element: "))
        arr.append(no)

    primes, result = ListPrime(arr)

    print("Prime numbers are:", primes)
    print("Addition of prime numbers is:", result)


if __name__ == "__main__":
    main()