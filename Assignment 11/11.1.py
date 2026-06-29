from Library_11 import isPrimex

def main():
    a=int(input("Enter your number:"))
    isPrimex(a)

    if isPrimex(a):
        print("Is prime number")
    else:
        print("Is not a prime number")

if __name__=="__main__":
    main()