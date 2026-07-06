import threading

def CheckNo(n):
    n=int(n)
    if n<0 :
        print("Negative Number")
    elif n>0 :
        print("Positive Number")
    elif n==0:
        print("Zero")
    
def main():
    no=(input("Enter number : "))
    t1=threading.Thread(target=CheckNo,args=(no,))
    t1.start()

if __name__=="__main__":
    main()
