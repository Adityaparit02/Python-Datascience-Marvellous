def patterndisplay(n):
    for i in range(n, 0, -1):
        print("* " * i)

def main():
    no=int(input("Enter number :"))
    patterndisplay(no)

if __name__=="__main__":
    main()