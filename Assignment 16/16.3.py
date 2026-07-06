import threading

def Add(a,b):
    sum=a+b
    print(sum)

def main():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number :"))
    t1=threading.Thread(target=Add,args=(a,b,))
    t1.start()
    print(t1)

if __name__=="__main__":
    main()