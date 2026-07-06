def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact

def main():
    no=int(input("Enter Number: "))
    ret=factorial(no)
    print(f"Factorial of {no} is {ret}")

if __name__=="__main__":
    main()