def adddigits(n):
    total = 0
    for digit in n:
        total = total + int(digit)
    return total


def main():
    no = input("Enter Value: ")
    ret = adddigits(no)
    print("Addition of digits is:", ret)
    

if __name__ == "__main__":
    main()
