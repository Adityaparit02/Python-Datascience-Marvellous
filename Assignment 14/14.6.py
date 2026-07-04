checkodd= lambda n : True if n%2!=0 else False

def main():
    a = int (input("Enter Number: "))
    b=checkodd(a)
    print(b)

if __name__=="__main__":
    main()