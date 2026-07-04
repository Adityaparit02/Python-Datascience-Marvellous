divisibleby5 = lambda n : True if n % 5 == 0 else False

def main():
    a= int(input("Enter number:"))
    b=divisibleby5(a)
    print(b)

if __name__=="__main__":
    main()