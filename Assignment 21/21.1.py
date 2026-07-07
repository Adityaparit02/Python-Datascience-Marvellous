import threading

def listmaker(n):
    arr=list()
    for i in range (1,n+1):
        value=int(input(f"Enter value {i} :"))
        arr.append(value)
    print(f"The list is : {arr}")
    return arr

def Prime(n):
    prime_list = []

    for value in n:
        if value <= 1:
            continue

        is_prime = True

        for i in range(2, value):
            if value % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(value)
    
    print(f"The list of prime numbers is: {list(prime_list)}")



def NonPrime(n):
    non_prime_list = []

    for value in n:
        if value <= 1:
            non_prime_list.append(value)
            continue

        is_prime = True

        for i in range(2, value):
            if value % i == 0:
                is_prime = False
                break

        if is_prime == False:
            non_prime_list.append(value)

    print(f"The list of non prime numbers is: {list(non_prime_list)}")


def main():
    no_elements = int(input("Enter number of elements to be inserted in list : "))
    listx=listmaker(no_elements)

    t1=threading.Thread(target=Prime,args=(listx,))
    t2=threading.Thread(target=NonPrime,args=(listx,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()
