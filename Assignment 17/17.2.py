def pattern(n):
    for i in range(n):
            print("*  "*n)

def main():
    no=int(input("Enter NUmber: "))
    pattern(no)

if __name__=="__main__":
    main()