def squarenumpattern(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def main():
    no=int(input("Enter Number: "))
    squarenumpattern(no)

if __name__=="__main__":
    main()