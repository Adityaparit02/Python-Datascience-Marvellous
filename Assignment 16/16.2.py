import threading

def ChkNum(n):
    if n%2==0:
        print("Even number")
    elif n%2!=0:
        print("Odd number")
    else :
        print("Invalid number")


def main():
    num=int(input("Enter number : "))
    t1=threading.Thread(target=ChkNum,args=(num,))
    t1.start()

if __name__=="__main__":
    main()