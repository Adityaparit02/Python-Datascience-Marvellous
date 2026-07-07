mult = lambda n,m : n*m

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    multiplication = mult(no1,no2)
    print(f"Multiplication of {no1} and {no2} is {multiplication}")


if __name__=="__main__":
    main()