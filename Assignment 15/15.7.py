from functools import reduce

strlen = lambda a, b: a if len(a) >= len(b) else b

def listmaker(n):
    arr = []

    for i in range(n):
        value = input("Enter string: ")
        arr.append(value)

    return arr

def main():
    no_elements = int(input("Enter no of elements to be inserted: "))
    listx = listmaker(no_elements)

    filtered_data = list(filter(lambda x: len(x) > 5, listx))

    if len(filtered_data) == 0:
        print("No string has length greater than 5.")
    else:
        RData = reduce(strlen, filtered_data)
        print("Longest string with length greater than 5:", RData)

if __name__ == "__main__":
    main()