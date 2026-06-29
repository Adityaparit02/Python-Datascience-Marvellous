def factorial(n):
    mult=1
    for i in range (1,n+1):
        mult=mult*i
    return print("Factorial of",n,"is",mult)

def main():
    a=int(input("Enter your number: "))
    factorial(a)

if __name__=="__main__":
    main()