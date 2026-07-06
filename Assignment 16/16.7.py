import threading

def divby5(n):
    n=int(n)
    if n%5==0:
        print(True)
    else :
        print(False)
    
def main():
    no=input("Enter Number: ")
    t1=threading.Thread(target=divby5,args=(no,))
    t1.start()
    print(t1)

if __name__=="__main__":
    main()
    