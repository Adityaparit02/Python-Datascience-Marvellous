def numcount(n):
    n=str(n)
    print(f"The length of {n} is {len(n)}")
    n=int(n)

def main():
    no=int(input("Enter Number: "))
    numcount(no)

if __name__=="__main__":
    main()