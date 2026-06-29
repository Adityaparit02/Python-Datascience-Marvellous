from Library_11 import palindrome

def main():
    num = int(input("Enter a number: "))

    if palindrome(num):
        print(num, "is a Palindrome")

    else:
        print(num, "is Not a Palindrome")

if __name__=="__main__":
    main()