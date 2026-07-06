import threading

def printstar(n):
    n=int(n)
    print("*  " * n, )

def main():
    no=input("Enter no of stars to print: ")
    t1=threading.Thread(target=printstar,args=(no,))
    t1.start()

if __name__=="__main__":
    main()