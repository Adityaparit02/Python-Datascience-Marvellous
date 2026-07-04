counteven = lambda x: x % 2 == 0

def listmaker(n):
    arr = []

    for i in range(n):
        value = int(input("Enter value: "))
        arr.append(value)

    return arr

def main():
    no_elements = int(input("Enter number of elements to insert: "))
    listx = listmaker(no_elements)

    FData = list(filter(counteven, listx))

    print("Even numbers are:", FData)
    print("Count of even numbers in list is:", len(FData))

if __name__ == "__main__":
    main()