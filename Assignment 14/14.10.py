largestno = lambda a, b, c: a if a >= b and a >= c else b if b >= a and b >= c else c

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    largen = largestno(a, b, c)
    print("Largest number is:", largen)

if __name__ == "__main__":
    main()